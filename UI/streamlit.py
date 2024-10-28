import streamlit as st
import requests

st.title("Service Update API Request Form")

# Placeholder lists for new and current services
new_services = []
current_services = []

# State to keep track of the number of services
if "new_services_count" not in st.session_state:
    st.session_state.new_services_count = 1
if "current_services_count" not in st.session_state:
    st.session_state.current_services_count = 1

# Function to create service input fields
def service_input_fields(service_number, prefix="new"):
    service_name = st.text_input(f"{prefix.capitalize()} Service {service_number} Name", key=f"{prefix}_name_{service_number}")
    service_url = st.text_input(f"{prefix.capitalize()} Service {service_number} URL", key=f"{prefix}_url_{service_number}")
    version_number = st.text_input(f"{prefix.capitalize()} Service {service_number} Version", key=f"{prefix}_version_{service_number}")
    return {
        "serviceName": service_name,
        "serviceUrl": service_url,
        "versionNumber": version_number
    }

# Section to add new services
st.subheader("New Services")
for i in range(st.session_state.new_services_count):
    new_services.append(service_input_fields(i + 1, prefix="new"))

if st.button("Add New Service", key="add_new_service"):
    st.session_state.new_services_count += 1

# Section to add current services
st.subheader("Current Services")
for i in range(st.session_state.current_services_count):
    current_services.append(service_input_fields(i + 1, prefix="current"))

if st.button("Add Current Service", key="add_current_service"):
    st.session_state.current_services_count += 1

# Submit form to API
if st.button("Send Request"):
    # Structure payload as required by API
    payload = {
        "requestId": "12345",
        "servicesDetails": {f"service_{i+1}": new_services[i] for i in range(st.session_state.new_services_count)},
        "currentServicesDetails": {f"service_{i+1}": current_services[i] for i in range(st.session_state.current_services_count)}
    }

    # Display the payload for user verification
    st.write("Payload to be sent:", payload)

    # Make the API call
    try:
        # Replace 'your_api_endpoint' with your actual API URL
        response = requests.post("http://localhost:8000/download-services-data", json=payload)
        print(response.json())
        # Display response
        if response.status_code == 200:
            st.success("Request sent successfully!")
            st.markdown(response.json())  # Display the JSON response
        else:
            st.error("Failed to send request. Status Code: " + str(response.status_code))
            st.json(response.json())  # Display the error response
    except Exception as e:
        st.error("An error occurred: " + str(e))

