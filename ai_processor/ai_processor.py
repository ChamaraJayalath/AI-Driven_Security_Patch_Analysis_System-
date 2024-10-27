from llama_index import VectorStoreIndex
from llama_index.embeddings import HuggingFaceEmbedding
from llama_index.llms.palm import PaLM
from llama_index import ServiceContext
import os
import pandas as pd
from llama_index import SimpleDirectoryReader
from utils.utils import OutputData
from scripts.logging_config import logger


class AIProcessor:
    @staticmethod
    def generate_report(scraper_data: OutputData):
        logger.info("Starting report generation process.")

        embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-large-en-v1.5")
        os.environ['GOOGLE_API_KEY'] = 'AIzaSyAFHH8CKaqIy0O4qQHSxLbb7iIsLn6eydg'
        llm = PaLM()

        try:
            # Load directories for new and current services
            new_services_directory = f"{scraper_data.directoryPath}/new_services/markdown"
            current_services_directory = f"{scraper_data.directoryPath}/current_services/markdown"
            logger.info(f"Loading documents from {new_services_directory} and {current_services_directory}.")

            new_services_documents = SimpleDirectoryReader(new_services_directory).load_data()
            current_services_documents = SimpleDirectoryReader(current_services_directory).load_data()
            logger.info("Documents loaded successfully.")

            # Create service context and indexes for both new and current services
            service_context = ServiceContext.from_defaults(llm=llm, embed_model=embed_model, chunk_size=800,
                                                           chunk_overlap=20)
            index1 = VectorStoreIndex.from_documents(new_services_documents, service_context=service_context,
                                                     show_progress=True)
            index2 = VectorStoreIndex.from_documents(current_services_documents, service_context=service_context,
                                                     show_progress=True)
            logger.info("Indexes created for new and current services.")

            # Persist indexes if needed for future reference
            index1.storage_context.persist()
            index2.storage_context.persist()
            logger.info("Indexes persisted.")

            # Initialize query engines for both indexes
            new_services_query_engine = index1.as_query_engine()
            current_services_query_engine = index2.as_query_engine()
            logger.info("Query engines initialized.")

            # Perform security analysis on new services
            logger.info("Analyzing new services for potential security risks.")
            new_services_analysis = new_services_query_engine.query(
                """
                For each new service, analyze potential security vulnerabilities, dependencies, and
                performance concerns that may impact current services. Summarize findings for each service.
                """
            )

            # Perform security analysis on current services to establish a baseline
            logger.info("Analyzing current services for baseline security concerns.")
            current_services_analysis = current_services_query_engine.query(
                """
                For each current service, identify existing security vulnerabilities, dependencies, and
                any critical functions that could be impacted by external services.
                """
            )

            # Compare new services' impacts on current services
            logger.info("Starting comparison of new and current services.")
            comparison_results = []
            for current_service in current_services_analysis:
                logger.info(f"Evaluating potential impacts on current service: {current_service['service_name']}")
                for new_service in new_services_analysis:
                    logger.info(f"Comparing with new service: {new_service['service_name']}")

                    # Perform a comparison analysis between new and current services
                    impact = AIProcessor.analyze_impact(new_service, current_service)
                    if impact:  # If there's a notable security impact
                        logger.info(f"Impact found for {current_service['service_name']} due to {new_service['service_name']}.")
                        comparison_results.append({
                            "Current Service": current_service["service_name"],
                            "Impact from New Service": new_service["service_name"],
                            "Potential Security Impact": impact["description"],
                            "Risk Level": impact["risk_level"],
                            "Recommendations": impact["recommendations"]
                        })

            logger.info("Comparison completed. Generating report.")
            return pd.DataFrame(comparison_results)

        except Exception as e:
            logger.error(f"Error generating report: {e}")
            return None

    @staticmethod
    def analyze_impact(new_service, current_service):
        """
        Compares a new service's details with a current service's to identify potential impacts.
        Returns a dictionary with impact description, risk level, and recommendations if any impact is detected.
        """
        from scripts.logging_config import logger
        logger.info(f"Analyzing impact between new service: {new_service['service_name']} and current service: {current_service['service_name']}")

        impact_details = {
            "description": "",
            "risk_level": "Low",  # Default risk level
            "recommendations": "None"
        }

        # Custom logic to analyze impact
        if "dependency" in new_service and new_service["dependency"] in current_service["dependencies"]:
            impact_details["description"] = "New service introduces dependency that may conflict with current service."
            impact_details["risk_level"] = "High"
            impact_details["recommendations"] = "Review and resolve dependency conflicts."
            logger.info(f"High-risk impact identified: {impact_details['description']}")

        # Add other checks as needed to build out impact details...

        return impact_details if impact_details["description"] else None
