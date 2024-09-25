






Release Notes








Release Notes
=============



Table of Contents
* [Keycloak 25\.0\.0](#keycloak-25-0-0)
	+ [Account Console v2 theme removed](#account-console-v2-theme-removed)
	+ [Java 21 support](#java-21-support)
	+ [Java 17 support is deprecated](#java-17-support-is-deprecated)
	+ [Most of Java adapters removed](#most-of-java-adapters-removed)
	+ [Upgrade to PatternFly 5](#upgrade-to-patternfly-5)
	+ [Argon2 password hashing](#argon2-password-hashing)
	+ [New Hostname options](#new-hostname-options)
	+ [Persistent user sessions](#persistent-user-sessions)
	+ [Cookies updates](#cookies-updates)
		- [SameSite attribute set for all cookies](#samesite-attribute-set-for-all-cookies)
		- [Removing KC\_AUTH\_STATE cookie](#removing-kc_auth_state-cookie)
	+ [Deprecated cookie methods removed](#deprecated-cookie-methods-removed)
	+ [Addressed 'You are already logged in' for expired authentication sessions](#addressed-you-are-already-logged-in-for-expired-authentication-sessions)
	+ [Lightweight access token to be even more lightweight](#lightweight-access-token-to-be-even-more-lightweight)
	+ [Support for application/jwt media\-type in token introspection endpoint](#support-for-applicationjwt-media-type-in-token-introspection-endpoint)
	+ [Password policy for check if password contains Username](#password-policy-for-check-if-password-contains-username)
	+ [Required actions improvements](#required-actions-improvements)
	+ [Passkeys improvements](#passkeys-improvements)
	+ [Default client profile for SAML](#default-client-profile-for-saml)
	+ [Authenticator for override existing IDP link during first\-broker\-login](#authenticator-for-override-existing-idp-link-during-first-broker-login)
	+ [OpenID for Verifiable Credential Issuance \- experimental support](#openid-for-verifiable-credential-issuance-experimental-support)
	+ [Searching by user attribute no longer case insensitive](#searching-by-user-attribute-no-longer-case-insensitive)
	+ [Breaking fix in authorization client library](#breaking-fix-in-authorization-client-library)
	+ [IDs are no longer set when exporting authorization settings for a client](#ids-are-no-longer-set-when-exporting-authorization-settings-for-a-client)
	+ [Management port for metrics and health endpoints](#management-port-for-metrics-and-health-endpoints)
	+ [Syslog for remote logging](#syslog-for-remote-logging)
	+ [Change to class `EnvironmentDependentProviderFactory`](#change-to-class-environmentdependentproviderfactory)
	+ [All `cache` options are runtime](#all-cache-options-are-runtime)
	+ [High availability guide enhanced](#high-availability-guide-enhanced)
	+ [Removing deprecated methods from `AccessToken`, `IDToken`, and `JsonWebToken` classes](#removing-deprecated-methods-from-accesstoken-idtoken-and-jsonwebtoken-classes)
	+ [Method `getExp` added to `SingleUseObjectKeyModel`](#method-getexp-added-to-singleuseobjectkeymodel)
	+ [Support for PostgreSQL 16](#support-for-postgresql-16)
	+ [Introducing support for Customer Identity and Access Management (CIAM) and Multi\-tenancy](#introducing-support-for-customer-identity-and-access-management-ciam-and-multi-tenancy)
* [Keycloak 24\.0\.5](#keycloak-24-0-5)
	+ [Security issue with PAR clients using client\_secret\_post based authentication](#security-issue-with-par-clients-using-client_secret_post-based-authentication)
* [Keycloak 24\.0\.4](#keycloak-24-0-4)
	+ [Partial update to user attributes when updating users through the Admin User API is no longer supported](#partial-update-to-user-attributes-when-updating-users-through-the-admin-user-api-is-no-longer-supported)
* [Keycloak 24\.0\.1](#keycloak-24-0-1)
	+ [Operator deploys nightly build instead of 24\.0\.0](#operator-deploys-nightly-build-instead-of-24-0-0)
* [Keycloak 24\.0\.0](#keycloak-24-0-0)
	+ [Supported user profile and progressive profiling](#supported-user-profile-and-progressive-profiling)
		- [Breaking changes to the User Profile SPI](#breaking-changes-to-the-user-profile-spi)
		- [Changes to Freemarker templates to render pages based on the user profile and realm](#changes-to-freemarker-templates-to-render-pages-based-on-the-user-profile-and-realm)
		- [New Freemarker template for the update profile page at first login through a broker](#new-freemarker-template-for-the-update-profile-page-at-first-login-through-a-broker)
	+ [Java adapter deprecation and removal](#java-adapter-deprecation-and-removal)
		- [Jetty adapter removed](#jetty-adapter-removed)
	+ [New Welcome Page](#new-welcome-page)
	+ [New Account Console now the default](#new-account-console-now-the-default)
	+ [Keycloak JS](#keycloak-js)
		- [Using `exports` field in `package.json`](#using-exports-field-in-package-json)
		- [PKCE enabled by default](#pkce-enabled-by-default)
	+ [Changes to Password Hashing](#changes-to-password-hashing)
	+ [OAuth/OIDC related improvements](#oauthoidc-related-improvements)
		- [Lightweight access tokens support](#lightweight-access-tokens-support)
		- [OAuth 2\.1 support](#oauth-2-1-support)
		- [Scope parameter supported in the refresh token flow](#scope-parameter-supported-in-the-refresh-token-flow)
		- [Client policy executor for secure redirect URIs](#client-policy-executor-for-secure-redirect-uris)
		- [Client policy executor for enforcing DPoP](#client-policy-executor-for-enforcing-dpop)
		- [Supporting EdDSA](#supporting-eddsa)
		- [EC Keys supported by JavaKeystore provider](#ec-keys-supported-by-javakeystore-provider)
		- [Option to add X509 thumbprint to JWT when using private\_key\_jwt authentication for identity providers](#option-to-add-x509-thumbprint-to-jwt-when-using-private_key_jwt-authentication-for-identity-providers)
		- [OAuth Grant Type SPI](#oauth-grant-type-spi)
	+ [CORS improvements](#cors-improvements)
	+ [Truststore improvements](#truststore-improvements)
	+ [Versioned Features](#versioned-features)
		- [Keycloak CR Truststores](#keycloak-cr-truststores)
		- [Trust Kubernetes CA](#trust-kubernetes-ca)
	+ [Automatic certificate management for SAML identity providers](#automatic-certificate-management-for-saml-identity-providers)
	+ [Non\-blocking health check for load balancers](#non-blocking-health-check-for-load-balancers)
	+ [Keycloak CR Optimized Field](#keycloak-cr-optimized-field)
	+ [Enhanced reverse proxy settings](#enhanced-reverse-proxy-settings)
	+ [Changes to the user representation in both Admin API and Account contexts](#changes-to-the-user-representation-in-both-admin-api-and-account-contexts)
	+ [Sequential loading of offline sessions and remote sessions](#sequential-loading-of-offline-sessions-and-remote-sessions)
	+ [Performing actions on behalf of another already authenticated user is not longer possible](#performing-actions-on-behalf-of-another-already-authenticated-user-is-not-longer-possible)
	+ [Changes to the email verification flow](#changes-to-the-email-verification-flow)
	+ [Deprecated offline session preloading](#deprecated-offline-session-preloading)
	+ [Configuration option for offline session lifespan override in memory](#configuration-option-for-offline-session-lifespan-override-in-memory)
	+ [Infinispan metrics use labels for cache manager and cache names](#infinispan-metrics-use-labels-for-cache-manager-and-cache-names)
	+ [User attribute value length extension](#user-attribute-value-length-extension)
	+ [Brute Force Protection changes](#brute-force-protection-changes)
	+ [Authorization Policy](#authorization-policy)
	+ [Keycloak CR cache\-config\-file option](#keycloak-cr-cache-config-file-option)
	+ [Keycloak CR resources options](#keycloak-cr-resources-options)
	+ [Temporary lockout log replaced with event](#temporary-lockout-log-replaced-with-event)
	+ [Updates to cookies](#updates-to-cookies)
	+ [SAML User Attribute Mapper For NameID now suggests only valid NameID formats](#saml-user-attribute-mapper-for-nameid-now-suggests-only-valid-nameid-formats)
	+ [Different JVM memory settings when running in a container](#different-jvm-memory-settings-when-running-in-a-container)
	+ [GELF log handler has been deprecated](#gelf-log-handler-has-been-deprecated)
	+ [Support for multi\-site active\-passive deployments](#support-for-multi-site-active-passive-deployments)
* [Keycloak 23\.0\.0](#keycloak-23-0-0)
	+ [OpenID Connect / OAuth 2\.0](#openid-connect-oauth-2-0)
		- [FAPI 2 drafts support](#fapi-2-drafts-support)
		- [DPoP preview support](#dpop-preview-support)
		- [More flexibility for introspection endpoint](#more-flexibility-for-introspection-endpoint)
		- [Feature flag for OAuth 2\.0 device authorization grant flow](#feature-flag-for-oauth-2-0-device-authorization-grant-flow)
	+ [Authentication](#authentication)
		- [Passkeys support](#passkeys-support)
		- [WebAuthn improvements](#webauthn-improvements)
		- [You are already logged\-in](#you-are-already-logged-in)
		- [Password policy for specify Maximum authentication time](#password-policy-for-specify-maximum-authentication-time)
	+ [Deployments](#deployments)
		- [Preview support for multi\-site active\-passive deployments](#preview-support-for-multi-site-active-passive-deployments)
	+ [Adapters](#adapters)
		- [OpenID Connect WildFly and JBoss EAP](#openid-connect-wildfly-and-jboss-eap)
		- [SAML WildFly and JBoss EAP](#saml-wildfly-and-jboss-eap)
	+ [Server distribution](#server-distribution)
		- [Load Shedding support](#load-shedding-support)
		- [RESTEasy Reactive](#resteasy-reactive)
	+ [User profile](#user-profile)
	+ [Group scalability](#group-scalability)
	+ [Themes](#themes)
		- [Localization files for themes default to UTF\-8 encoding](#localization-files-for-themes-default-to-utf-8-encoding)
	+ [Storage](#storage)
		- [Removal of the Map Store](#removal-of-the-map-store)
* [Keycloak 22\.0\.3](#keycloak-22-0-3)
	+ [Security vulnerability when registering or updating user through templates](#security-vulnerability-when-registering-or-updating-user-through-templates)
		- [Custom user storage providers](#custom-user-storage-providers)
* [Keycloak 22\.0\.2](#keycloak-22-0-2)
	+ [Improvements in LDAP and Kerberos integration](#improvements-in-ldap-and-kerberos-integration)
* [Keycloak 22\.0\.0](#keycloak-22-0-0)
	+ [Server Distribution](#server-distribution-2)
		- [Java 11 support removed](#java-11-support-removed)
		- [Upgrade to Quarkus 3\.x](#upgrade-to-quarkus-3-x)
		- [Upgrade to Hibernate ORM 6](#upgrade-to-hibernate-orm-6)
		- [Elytron credential store replacement](#elytron-credential-store-replacement)
		- [KeyStore Config Source added](#keystore-config-source-added)
		- [Hostname debug tool](#hostname-debug-tool)
		- [Passthrough proxy mode changes](#passthrough-proxy-mode-changes)
		- [Export and Import perform an automatic build](#export-and-import-perform-an-automatic-build)
	+ [Admin Console](#admin-console)
		- [Account Console v1 removal](#account-console-v1-removal)
		- [Account Console v3 promoted to preview](#account-console-v3-promoted-to-preview)
		- [Account Console template variables removed](#account-console-template-variables-removed)
		- [Changes to custom Admin Console messages](#changes-to-custom-admin-console-messages)
	+ [JavaScript adapter](#javascript-adapter)
		- [Legacy Promise API removed](#legacy-promise-api-removed)
		- [Required to be instantiated with the `new` operator](#required-to-be-instantiated-with-the-new-operator)
	+ [Admin API](#admin-api)
		- [Renamed Admin library artifacts](#renamed-admin-library-artifacts)
		- [Support for count users based on custom attributes](#support-for-count-users-based-on-custom-attributes)
	+ [Operator](#operator)
		- [k8s.keycloak.org/v2alpha1 changes](#k8s-keycloak-orgv2alpha1-changes)
		- [Co\-management of Operator Resources](#co-management-of-operator-resources)
	+ [Identity Brokering](#identity-brokering)
		- [Essential claim configuration in OpenID Connect identity providers](#essential-claim-configuration-in-openid-connect-identity-providers)
		- [Support for JWE encrypted ID Tokens and UserInfo responses in OpenID Connect providers](#support-for-jwe-encrypted-id-tokens-and-userinfo-responses-in-openid-connect-providers)
		- [Hardcoded group mapper](#hardcoded-group-mapper)
		- [User session note mapper](#user-session-note-mapper)
	+ [LDAP Federation](#ldap-federation)
		- [LDAPS\-only Truststore option removed](#ldaps-only-truststore-option-removed)
	+ [Removed Openshift integration feature](#removed-openshift-integration-feature)
* [Keycloak 21\.1\.2](#keycloak-21-1-2)
	+ [Changes in validating schemes for valid redirect URIs](#changes-in-validating-schemes-for-valid-redirect-uris)
* [Keycloak 21\.1\.0](#keycloak-21-1-0)
	+ [Monorepo](#monorepo)
	+ [FIPS 140\-2 support](#fips-140-2-support)
	+ [Experimental Account Console version 3](#experimental-account-console-version-3)
	+ [Changes to Keycloak Authorization Services support in Keycloak Java\-based Adapters](#changes-to-keycloak-authorization-services-support-in-keycloak-java-based-adapters)
* [Keycloak 21\.0\.0](#keycloak-21-0-0)
	+ [Old Admin Console removed](#old-admin-console-removed)
	+ [Keycloak uses Micrometer for metrics](#keycloak-uses-micrometer-for-metrics)
	+ [Java 11 support for Keycloak server deprecated](#java-11-support-for-keycloak-server-deprecated)
	+ [Hashicop Vault no longer supported](#hashicop-vault-no-longer-supported)
	+ [SAML SP metadata changes](#saml-sp-metadata-changes)
	+ [Deprecated methods from user session provider were removed](#deprecated-methods-from-user-session-provider-were-removed)
	+ [New storage: `IS_CLIENT_ROLE` searchable field was deprecated](#new-storage-is_client_role-searchable-field-was-deprecated)
	+ [FIPS 140\-2 preview support](#fips-140-2-preview-support)
	+ [Support for the standard `Forwarded` header when running behind a reverse proxy](#support-for-the-standard-forwarded-header-when-running-behind-a-reverse-proxy)
	+ [The container image is now based on ubi9\-micro](#the-container-image-is-now-based-on-ubi9-micro)
	+ [Other improvements](#other-improvements)
* [Keycloak 20\.0\.0](#keycloak-20-0-0)
	+ [WildFly distribution removed](#wildfly-distribution-removed)
	+ [New Keycloak Operator upgrade](#new-keycloak-operator-upgrade)
		- [Realm Operator](#realm-operator)
	+ [Supported OpenJDK versions](#supported-openjdk-versions)
	+ [Hostname provider now supports configuring the complete base URL](#hostname-provider-now-supports-configuring-the-complete-base-url)
	+ [Improvements to `kc.bat` when running Keycloak on Windows](#improvements-to-kc-bat-when-running-keycloak-on-windows)
	+ [Upgrade of embedded H2 database](#upgrade-of-embedded-h2-database)
	+ [Feature guard for hosting the Keycloak JavaScript adapter](#feature-guard-for-hosting-the-keycloak-javascript-adapter)
	+ [OTP Application SPI](#otp-application-spi)
	+ [Custom Identity Providers can now set an icon for the provider](#custom-identity-providers-can-now-set-an-icon-for-the-provider)
	+ [FIPS 140\-2 experimental support](#fips-140-2-experimental-support)
	+ [Search groups by attribute](#search-groups-by-attribute)
	+ [View group membership in the account console](#view-group-membership-in-the-account-console)
	+ [Deprecated methods from data providers and models were removed](#deprecated-methods-from-data-providers-and-models-were-removed)
* [Keycloak 19\.0\.0](#keycloak-19-0-0)
	+ [OpenID Connect and SAML Adapters End\-of\-life](#openid-connect-and-saml-adapters-end-of-life)
		- [Fuse 6 and 7 (OpenID Connect)](#fuse-6-and-7-openid-connect)
		- [JBoss AS 7 and EAP 6 (OpenID Connect and SAML)](#jboss-as-7-and-eap-6-openid-connect-and-saml)
		- [Jetty 9\.2 and 9\.3 (OpenID Connect and SAML)](#jetty-9-2-and-9-3-openid-connect-and-saml)
		- [Spring Boot 1 (OpenID Connect)](#spring-boot-1-openid-connect)
		- [WildFly legacy security layer (OpenID Connect and SAML)](#wildfly-legacy-security-layer-openid-connect-and-saml)
	+ [New Admin Console graduation](#new-admin-console-graduation)
	+ [Changes in Keycloak storage](#changes-in-keycloak-storage)
	+ [OIDC Logout changes](#oidc-logout-changes)
	+ [Update Email Workflow](#update-email-workflow)
	+ [Deprecated `podDisruptionBudget` in the legacy Keycloak Operator](#deprecated-poddisruptionbudget-in-the-legacy-keycloak-operator)
	+ [Initial Support for centralized logging](#initial-support-for-centralized-logging)
* [Keycloak 18\.0\.0](#keycloak-18-0-0)
	+ [New Operator preview](#new-operator-preview)
		- [OperatorHub versioning scheme](#operatorhub-versioning-scheme)
	+ [New Admin Console preview](#new-admin-console-preview)
	+ [Step\-up authentication](#step-up-authentication)
	+ [Client secret rotation](#client-secret-rotation)
	+ [Recovery Codes](#recovery-codes)
	+ [OpenID Connect Logout Improvements](#openid-connect-logout-improvements)
	+ [WebAuthn improvements](#webauthn-improvements-2)
	+ [The deprecated `upload-script` feature was removed](#the-deprecated-upload-script-feature-was-removed)
	+ [Session limits](#session-limits)
	+ [SAML ECP Profile is disabled by default](#saml-ecp-profile-is-disabled-by-default)
	+ [Quarkus distribution](#quarkus-distribution)
		- [Import realms at startup](#import-realms-at-startup)
		- [JSON and File Logging improvements](#json-and-file-logging-improvements)
		- [New Option db\-url\-port](#new-option-db-url-port)
		- [Split metrics\-enabled option into health\-enabled and metrics\-enabled](#split-metrics-enabled-option-into-health-enabled-and-metrics-enabled)
	+ [Other improvements](#other-improvements-2)
* [Keycloak 17\.0\.0](#keycloak-17-0-0)
	+ [Highlights](#highlights)
		- [Quarkus distribution is now fully supported](#quarkus-distribution-is-now-fully-supported)
		- [Quarkus distribution updates](#quarkus-distribution-updates)
		- [Other improvements](#other-improvements-3)
* [Keycloak 16\.1\.0](#keycloak-16-1-0)
	+ [Highlights](#highlights-2)
		- [Upgrade to Wildfly 26\.0\.0](#upgrade-to-wildfly-26-0-0)
* [Keycloak 16\.0\.0](#keycloak-16-0-0)
	+ [Highlights](#highlights-3)
		- [Upgrade to Wildfly 25\.0\.1](#upgrade-to-wildfly-25-0-1)
		- [Upgrade to Quarkus 2\.5\.3](#upgrade-to-quarkus-2-5-3)
* [Keycloak 15\.1\.0](#keycloak-15-1-0)
	+ [Highlights](#highlights-4)
		- [Quarkus distribution preview](#quarkus-distribution-preview)
		- [New Admin Console preview](#new-admin-console-preview-2)
		- [WildFly update](#wildfly-update)
		- [WildFly adapter deprecation](#wildfly-adapter-deprecation)
		- [Spring Security and Boot adapter deprecation](#spring-security-and-boot-adapter-deprecation)
		- [OpenID Connect Front\-Channel Logout Support](#openid-connect-front-channel-logout-support)
		- [Deprecated features in the Keycloak Operator](#deprecated-features-in-the-keycloak-operator)
* [Keycloak 15\.0\.1](#keycloak-15-0-1)
	+ [Highlights](#highlights-5)
* [Keycloak 15\.0\.0](#keycloak-15-0-0)
	+ [Highlights](#highlights-6)
		- [Financial\-grade API (FAPI) Improvements, FAPI CIBA and Open Banking Brasil](#financial-grade-api-fapi-improvements-fapi-ciba-and-open-banking-brasil)
* [Keycloak 14\.0\.0](#keycloak-14-0-0)
	+ [Highlights](#highlights-7)
		- [Client Policies and Financial\-grade API (FAPI) Support](#client-policies-and-financial-grade-api-fapi-support)
		- [Improvements to User Profile SPI and support for declarative configuration](#improvements-to-user-profile-spi-and-support-for-declarative-configuration)
		- [Improvements to offline sessions](#improvements-to-offline-sessions)
		- [Other improvements](#other-improvements-4)
* [Keycloak 13\.0\.0](#keycloak-13-0-0)
	+ [Highlights](#highlights-8)
		- [Upgrade to Wildfly 23](#upgrade-to-wildfly-23)
		- [OAuth 2\.0 Device Authorization Grant (RFC 8628\)](#oauth-2-0-device-authorization-grant-rfc-8628)
		- [OpenID Connect Client Initiated Backchannel Authentication (CIBA)](#openid-connect-client-initiated-backchannel-authentication-ciba)
		- [SAML Artifact binding in server to client communication](#saml-artifact-binding-in-server-to-client-communication)
		- [Support PKCE for identity brokering](#support-pkce-for-identity-brokering)
		- [Default roles processing improvement](#default-roles-processing-improvement)
* [Keycloak 12\.0\.0](#keycloak-12-0-0)
	+ [Highlights](#highlights-9)
		- [Keycloak.X distribution preview](#keycloak-x-distribution-preview)
		- [New Account console is now the default](#new-account-console-is-now-the-default)
		- [OpenID Connect Back\-Channel Logout](#openid-connect-back-channel-logout)
		- [Upgrade to Wildfly 21](#upgrade-to-wildfly-21)
		- [Ability to request AuthnContext in SAML identity provider](#ability-to-request-authncontext-in-saml-identity-provider)
		- [FAPI RW support and initial support to Client policies](#fapi-rw-support-and-initial-support-to-client-policies)
		- [Upgrade login theme to PatternFly 4](#upgrade-login-theme-to-patternfly-4)
		- [Gatekeeper EOL](#gatekeeper-eol)
		- [Other improvements](#other-improvements-5)
* [Keycloak 11\.0\.0](#keycloak-11-0-0)
	+ [Highlights](#highlights-10)
		- [LDAPv3 password modify operation](#ldapv3-password-modify-operation)
		- [Namespace support for LDAP group mapper](#namespace-support-for-ldap-group-mapper)
		- [Upgrade to WildFly 20](#upgrade-to-wildfly-20)
		- [SAML POST binding is broken in the latest versions of browsers](#saml-post-binding-is-broken-in-the-latest-versions-of-browsers)
		- [Other improvements](#other-improvements-6)
* [Keycloak 10\.0\.0](#keycloak-10-0-0)
	+ [Highlights](#highlights-11)
		- [Identity Brokering Sync Mode](#identity-brokering-sync-mode)
		- [Client Session Timeout for OpenID Connect / OAuth 2\.0](#client-session-timeout-for-openid-connect-oauth-2-0)
		- [OAuth 2\.0 Token Revocation (RFC 7009\)](#oauth-2-0-token-revocation-rfc-7009)
		- [Security Headers SPI and Response Filter](#security-headers-spi-and-response-filter)
		- [Upgrade to WildFly 19](#upgrade-to-wildfly-19)
		- [Other improvements](#other-improvements-7)
* [Keycloak 9\.0\.1](#keycloak-9-0-1)
	+ [Highlights](#highlights-12)
		- [PromiseType removed from JavaScript adapter](#promisetype-removed-from-javascript-adapter)
	+ [Other improvements](#other-improvements-8)
		- [Reverted breaking API changes to LocaleSelectorSPI](#reverted-breaking-api-changes-to-localeselectorspi)
		- [Fixed the automatic resolution of `KeycloakConfigResolver` instances for Spring Boot Applications](#fixed-the-automatic-resolution-of-keycloakconfigresolver-instances-for-spring-boot-applications)
* [Keycloak 9\.0\.0](#keycloak-9-0-0)
	+ [Highlights](#highlights-13)
		- [Drools Policy Removed](#drools-policy-removed)
		- [Pagination support for clients](#pagination-support-for-clients)
		- [New Elytron Credential Store Vault Provider](#new-elytron-credential-store-vault-provider)
		- [More updates to W3C WebAuthn and Authentication flows](#more-updates-to-w3c-webauthn-and-authentication-flows)
		- [Improved handling of user locale](#improved-handling-of-user-locale)
		- [Other improvements](#other-improvements-9)
* [Keycloak 8\.0\.2](#keycloak-8-0-2)
	+ [Highlights](#highlights-14)
		- [SameSite cookie changes with upcoming Google Chrome update](#samesite-cookie-changes-with-upcoming-google-chrome-update)
* [Keycloak 8\.0\.1](#keycloak-8-0-1)
	+ [Highlights](#highlights-15)
		- [LDAP Issue](#ldap-issue)
		- [WildFly 18\.0\.1\.Final](#wildfly-18-0-1-final)
* [Keycloak 8\.0\.0](#keycloak-8-0-0)
	+ [Highlights](#highlights-16)
		- [Vault](#vault)
		- [New Default Hostname provider](#new-default-hostname-provider)
		- [Messages in theme resources](#messages-in-theme-resources)
		- [RoleMappingsProvider SPI for the SAML adapters](#rolemappingsprovider-spi-for-the-saml-adapters)
		- [WildFly 18 Upgrade](#wildfly-18-upgrade)
		- [W3C Web Authentication support](#w3c-web-authentication-support)
		- [Support for password\-less authentication, multi\-factor authentication and multiple credentials per user](#support-for-password-less-authentication-multi-factor-authentication-and-multiple-credentials-per-user)
	+ [Other Improvements](#other-improvements-10)
		- [System properties and environment variables support in theme.properties](#system-properties-and-environment-variables-support-in-theme-properties)
		- [Support more signing algorithms for client authentication with signed JWT](#support-more-signing-algorithms-for-client-authentication-with-signed-jwt)
		- [Configurable client authentication method for OIDC Identity providers](#configurable-client-authentication-method-for-oidc-identity-providers)
		- [Support enable/disable logging into the JavaScript adapter](#support-enabledisable-logging-into-the-javascript-adapter)
		- [Credentials support removed from the JavaScript adapter](#credentials-support-removed-from-the-javascript-adapter)
		- [Updates for Gatekeeper](#updates-for-gatekeeper)
		- [Deploying Scripts to the Server](#deploying-scripts-to-the-server)
* [Keycloak 7\.0\.1](#keycloak-7-0-1)
	+ [Deploying Scripts to the Server](#deploying-scripts-to-the-server-2)
* [Keycloak 7\.0\.0](#keycloak-7-0-0)
	+ [Highlights](#highlights-17)
		- [WildFly 17 Upgrade](#wildfly-17-upgrade)
		- [Tomcat 9 adapter support](#tomcat-9-adapter-support)
		- [New Account Console](#new-account-console)
		- [Signed and Encrypted ID Token Support](#signed-and-encrypted-id-token-support)
		- [Testing and release automation](#testing-and-release-automation)
	+ [Other improvements](#other-improvements-11)
* [Keycloak 6\.0\.0](#keycloak-6-0-0)
	+ [WildFly 16 Upgrade](#wildfly-16-upgrade)
		- [SmallRye Health and Metrics extensions](#smallrye-health-and-metrics-extensions)
	+ [PS256 support](#ps256-support)
	+ [MP\-JWT Client Scope](#mp-jwt-client-scope)
* [Keycloak 5\.0\.0](#keycloak-5-0-0)
	+ [WildFly 15 Upgrade](#wildfly-15-upgrade)
* [Keycloak 4\.8\.0\.Final](#keycloak-4-8-0-final)
	+ [OpenShift Integration](#openshift-integration)
	+ [Rules/Drools Policy Marked as a Technology Preview Feature](#rulesdrools-policy-marked-as-a-technology-preview-feature)
	+ [Support for DB2 removed](#support-for-db2-removed)
* [Keycloak 4\.7\.0\.Final](#keycloak-4-7-0-final)
	+ [Enhanced Remember Me](#enhanced-remember-me)
	+ [Pagination support for Groups](#pagination-support-for-groups)
	+ [Improve startup time with large number of offline sessions](#improve-startup-time-with-large-number-of-offline-sessions)
* [Keycloak 4\.6\.0\.Final](#keycloak-4-6-0-final)
	+ [Upgrade to WildFly 14](#upgrade-to-wildfly-14)
	+ [Keycloak Gatekeeper](#keycloak-gatekeeper)
* [Keycloak 4\.5\.0\.Final](#keycloak-4-5-0-final)
	+ [Signature SPI](#signature-spi)
	+ [New Signature Algorithms](#new-signature-algorithms)
	+ [Better Audience Support for OpenID Connect clients](#better-audience-support-for-openid-connect-clients)
	+ [Minor improvements](#minor-improvements)
* [Keycloak 4\.4\.0\.Final](#keycloak-4-4-0-final)
	+ [Upgrade to WildFly 13](#upgrade-to-wildfly-13)
	+ [Authorization Services support in Node.js](#authorization-services-support-in-node-js)
	+ [Minor improvements](#minor-improvements-2)
* [Keycloak 4\.3\.0\.Final](#keycloak-4-3-0-final)
	+ [Hostname SPI](#hostname-spi)
	+ [X509 Client Authenticator](#x509-client-authenticator)
	+ [Performance improvements to Authorization Services](#performance-improvements-to-authorization-services)
	+ [Choosing the response mode when obtaining permissions from the server](#choosing-the-response-mode-when-obtaining-permissions-from-the-server)
	+ [NodeJS Policy Enforcer](#nodejs-policy-enforcer)
	+ [Support hosted domain for Google logins](#support-hosted-domain-for-google-logins)
	+ [Escape unsafe tags in HTML output](#escape-unsafe-tags-in-html-output)
* [Keycloak 4\.2\.0\.Final](#keycloak-4-2-0-final)
	+ [Browser tab support for Cordova](#browser-tab-support-for-cordova)
	+ [SAML adapter multitenancy support](#saml-adapter-multitenancy-support)
	+ [An option to create claims with dots (.) in them](#an-option-to-create-claims-with-dots-in-them)
* [Keycloak 4\.1\.0\.Final](#keycloak-4-1-0-final)
	+ [Making Spring Boot 2 the default starter](#making-spring-boot-2-the-default-starter)
* [Keycloak 4\.0\.0\.Final](#keycloak-4-0-0-final)
	+ [Client Scopes and support for OAuth 2 scope parameter](#client-scopes-and-support-for-oauth-2-scope-parameter)
	+ [OAuth 2 Certificate Bound Access Tokens](#oauth-2-certificate-bound-access-tokens)
	+ [Authorization Services](#authorization-services)
		- [UMA 2\.0 Support](#uma-2-0-support)
		- [Pushed Claims](#pushed-claims)
		- [Resource Attributes](#resource-attributes)
		- [Policy enforcer now accepts regular access tokens](#policy-enforcer-now-accepts-regular-access-tokens)
		- [Policy enforcer can now load resources from the server on\-demand](#policy-enforcer-can-now-load-resources-from-the-server-on-demand)
		- [Policy enforcer now supports configuring the resource cache](#policy-enforcer-now-supports-configuring-the-resource-cache)
		- [Claim Information Points](#claim-information-points)
		- [Improvements to the Evaluation API](#improvements-to-the-evaluation-api)
	+ [Authorization Services](#authorization-services-2)
		- [UMA 2\.0](#uma-2-0)
		- [Pushed Claims](#pushed-claims-2)
		- [Resource Attributes](#resource-attributes-2)
	+ [Themes and Theme Resources](#themes-and-theme-resources)
	+ [Instagram Identity Provider](#instagram-identity-provider)
	+ [Search by User ID in Admin Console](#search-by-user-id-in-admin-console)
	+ [Adapters](#adapters-2)
		- [Spring Boot 2](#spring-boot-2)
		- [Fuse 7](#fuse-7)
		- [JavaScript \- Native Promise Support](#javascript-native-promise-support)
		- [JavaScript \- Cordova Options](#javascript-cordova-options)










**Release Notes** 




* [Getting Started](https://www.keycloak.org/guides#getting-started)
* [Securing Apps](https://www.keycloak.org/docs/25.0.6/securing_apps/)
* [Server Administration](https://www.keycloak.org/docs/25.0.6/server_admin/)
* [Server Developer](https://www.keycloak.org/docs/25.0.6/server_development/)
* [Authorization Services](https://www.keycloak.org/docs/25.0.6/authorization_services/)
* [Upgrading](https://www.keycloak.org/docs/25.0.6/upgrading/)








Version **25\.0\.6**








Keycloak 25\.0\.0
-----------------




### Account Console v2 theme removed



The Account Console v2 theme has been removed from Keycloak. This theme was deprecated in Keycloak 24 and replaced by the Account Console v3 theme. If you are still using this theme, you should migrate to the Account Console v3 theme.





### Java 21 support



Keycloak now supports OpenJDK 21, as we want to stick to the latest LTS OpenJDK versions.





### Java 17 support is deprecated



OpenJDK 17 support is deprecated in Keycloak, and will be removed in a following release in favor of OpenJDK 21\.





### Most of Java adapters removed



As stated in the release notes of previous Keycloak version, the most of Java adapters are now removed from the Keycloak codebase and downloads pages.




For OAuth 2\.0/OIDC, this includes removal of the Tomcat adapter, WildFly/EAP adapter, Servlet Filter adapter, `KeycloakInstalled` desktop adapter, the `jaxrs-oauth-client` adapter, JAAS login modules, Spring adapter and SpringBoot adapters.
You can check [our older post](https://www.keycloak.org/2023/03/adapter-deprecation-update.html) for the list of some alternatives.




For SAML, this includes removal of the Tomcat adapter and Servlet filter adapter. SAML adapters are still supported with WildFly and JBoss EAP.




The generic Authorization Client library is still supported, and we still plan to support it. It aims to be used in combination with any other OAuth 2\.0 or OpenID Connect libraries. You can
check the [quickstarts](https://github.com/keycloak/keycloak-quickstarts) for some examples where this authorization client library is used together with the 3rd party Java adapters like
Elytron OIDC or SpringBoot. You can check the quickstarts also for the example of SAML adapter used with WildFly.





### Upgrade to PatternFly 5



In Keycloak 24, the Welcome page is updated to use [PatternFly 5](https://www.patternfly.org/), the latest version of the design system that underpins the user interface of Keycloak. In this release, the Admin Console and Account Console are also updated to use PatternFly 5\. If you want to extend and customize the Admin Console and Account Console, review [the changes in PatternFly 5](https://www.patternfly.org/get-started/upgrade/) and update your customizations accordingly.





### Argon2 password hashing



Argon2 is now the default password hashing algorithm used by Keycloak in a non\-FIPS environment.




Argon2 was the winner of the [2015 password hashing competition](https://en.wikipedia.org/wiki/Password_Hashing_Competition)
and is the recommended hashing algorithm by [OWASP](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#argon2id).




In Keycloak 24 the default hashing iterations for PBKDF2 were increased from 27\.5K to 210K, resulting in a more than
10 times increase in the amount of CPU time required to generate a password hash. With Argon2 it is possible to achieve
better security, with almost the same CPU time as previous releases of Keycloak. One downside is Argon2 requires more
memory, which is a requirement to be resistant against GPU attacks. The defaults for Argon2 in Keycloak requires 7MB
per\-hashing request.
To prevent excessive memory and CPU usage, the parallel computation of hashes by Argon2 is by default limited to the number of cores available to the JVM.
To support the memory intensive nature of Argon2, we have updated the default GC from ParallelGC to G1GC for a better heap utilization.





### New Hostname options



In response to the complexity and lack of intuitiveness experienced with previous hostname configuration settings, we are proud to introduce Hostname v2 options.




We have listened to your feedback, tackled the tricky issues, and created a smoother experience for managing hostname configuration.
Be aware that even the behavior behind these options has changed and requires your attention \- if you are dealing with custom hostname settings.




Hostname v2 options are supported by default, as the old hostname options are deprecated and will be removed in the following releases.
You should migrate to them as soon as possible.




New options are activated by default, so Keycloak will not recognize the old ones.




For information on how to migrate, see the [Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/).





### Persistent user sessions



Previous versions of Keycloak stored only offline user and offline client sessions in the databases.
The new feature `persistent-user-sessions` stores online user sessions and online client sessions not only in memory, but also in the database.
This will allow a user to stay logged in even if all instances of Keycloak are restarted or upgraded.




The feature is a preview feature and disabled by default. To use it, add the following to your build command:






```
bin/kc.sh build --features=persistent-user-sessions ...
```




For more details see the [Enabling and disabling features](https://www.keycloak.org/server/features) guide.
The [sizing guide](https://www.keycloak.org/high-availability/concepts-memory-and-cpu-sizing) contains a new paragraph describing the updated resource requirements when this feature is enabled.




For information on how to upgrade, see the [Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/).





### Cookies updates



#### SameSite attribute set for all cookies



The following cookies did not use to set the `SameSite` attribute, which in recent browser versions results in them
defaulting to `SameSite=Lax`:




* `KC_STATE_CHECKER` now sets `SameSite=Strict`
* `KC_RESTART` now sets `SameSite=None`
* `KEYCLOAK_LOCALE` now sets `SameSite=None`
* `KEYCLOAK_REMEMBER_ME` now sets `SameSite=None`




The default value `SameSite=Lax` causes issues with POST based bindings, mostly applicable to SAML, but also used in
some OpenID Connect / OAuth 2\.0 flows.





#### Removing KC\_AUTH\_STATE cookie



The cookie `KC_AUTH_STATE` is removed and it is no longer set by the Keycloak server as this server no longer needs this cookie.






### Deprecated cookie methods removed



The following APIs for setting custom cookies have been removed:




* `ServerCookie` \- replaced by `NewCookie.Builder`
* `LocaleSelectorProvider.KEYCLOAK_LOCALE` \- replaced by `CookieType.LOCALE`
* `HttpCookie` \- replaced by `NewCookie.Builder`
* `HttpResponse.setCookieIfAbsent(HttpCookie cookie)` \- replaced by `HttpResponse.setCookieIfAbsent(NewCookie cookie)`





### Addressed 'You are already logged in' for expired authentication sessions



The Keycloak 23 release provided improvements for when a user is authenticated in parallel in multiple browser tabs. However, this improvement did not address the case when an authentication session
expired. Now for the case when user is already logged\-in in one browser tab and an authentication session expired in other browser tabs, Keycloak is able to redirect back to the client
application with an OIDC/SAML error, so the client application can immediately retry authentication, which should usually automatically log in the application because of the SSO session. For more
details, see [Server Administration Guide authentication sessions](https://www.keycloak.org/docs/25.0.6/server_admin/#_authentication-sessions).





### Lightweight access token to be even more lightweight



In previous releases, the support for lightweight access token was added. In this release, we managed to remove even more built\-in claims from the lightweight access token. The claims are added
by protocol mappers. Some of them affect even the regular access tokens or ID tokens as they were not strictly required by the OIDC specification.




* Claims `sub` and `auth_time` are added by protocol mappers now, which are configured by default on the new client scope `basic`, which is added automatically to all the clients. The claims are still added to the ID token and access token as before, but not to lightweight access token.
* Claim `nonce` is added only to the ID token now. It is not added to a regular access token or lightweight access token. For backwards compatibility, you can add this claim to an access token by protocol mapper, which needs to be explicitly configured.
* Claim `session_state` is not added to any token now. It is still possible to add it by protocol mapper if needed. There is still the other dedicated claim `sid` supported by the specification, which was available in previous versions as well and which has exactly the same value.




For more details, see the [Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/)..





### Support for application/jwt media\-type in token introspection endpoint



You can use the HTTP Header `Accept: application/jwt` when invoking a token introspection endpoint. When enabled for a particular client, it returns a claim `jwt` from the
token introspection endpoint with the full JWT access token, which can be useful especially for the use\-cases when the client calling introspection endpoint used lightweight access
token. Thanks to [Thomas Darimont](https://github.com/thomasdarimont) for the contribution.





### Password policy for check if password contains Username



Keycloak supports a new password policy that allows you to deny user passwords which contains the user username.





### Required actions improvements



In the Admin Console, you can now configure some required actions in the **Required actions** tab of a particular realm. Currently, the **Update password** is the only built\-in configurable required action. It supports setting **Maximum Age of Authentication**, which is the maximum time users can update their password
by the `kc_action` parameter (used for instance when updating password in the Account Console) without re\-authentication. The sorting of required actions is also improved. When there are multiple required
actions during authentication, all actions are sorted together regardless of whether those are actions set during authentication (for instance by the `kc_action` parameter) or actions added to the user account manually by an administrator.
Thanks to [Thomas Darimont](https://github.com/thomasdarimont) and [Daniel Fesenmeyer](https://github.com/danielFesenmeyer) for the contributions.





### Passkeys improvements



The support for Passkeys conditional UI was added. When the Passkeys preview feature is enabled, there is a dedicated authenticator available, which means you can select from a list of available passkeys accounts
and authenticate a user based on that. Thanks to [Takashi Norimatsu](https://github.com/tnorimat) for the contribution.





### Default client profile for SAML



The default client profile to have secured SAML clients was added. When browsing through client policies of a realm in the Admin Console, you see a new client profile `saml-security-profile`. When it is used, there are
security best practices applied for SAML clients such as signatures are enforced, SAML Redirect binding is disabled, and wildcard redirect URLs are prohibited.





### Authenticator for override existing IDP link during first\-broker\-login



There was new authenticator `Confirm override existing link` added. This authenticator allows to override linked IDP username for the Keycloak user, which was already linked to different
IDP identity before. More details in the [Server Administration Guide](https://www.keycloak.org/docs/25.0.6/server_admin/#_override_existing_broker_link). Thanks to [Lex Cao](https://github.com/lexcao) for the contribution.





### OpenID for Verifiable Credential Issuance \- experimental support



There is work in progress on the support of OpenID for Verifiable Credential Issuance (OID4VCI). Right now, this is still work in progress, but things are being gradually added. Keycloak
can act as an OID4VC Issuer with support of Pre\-Authorized code flow. There is support for verifiable credentials in the JWT\-VC, SD\-JWT\-VC and VCDM formats. Thanks to the members of the OAuth SIG
groups for the contributions and feedback and especially thanks to [Stefan Wiedemann](https://github.com/wistefan), [Francis Pouatcha](https://github.com/francis-pouatcha), [Takashi Norimatsu](https://github.com/tnorimat)
and [Yutaka Obuchi](https://github.com/bucchi).





### Searching by user attribute no longer case insensitive



When searching for users by user attribute, Keycloak no longer searches for user attribute names forcing lower case comparisons. The goal of this change was to speed up searches by using Keycloak’s native index on the user attribute table. If your database collation is case\-insensitive, your search results will stay the same. If your database collation is case\-sensitive, you might see less search results than before.





### Breaking fix in authorization client library



For users of the `keycloak-authz-client` library, calling `AuthorizationResource.getPermissions(…​)` now correctly returns a `List<Permission>`.




Previously, it would return a `List<Map>` at runtime, even though the method declaration advertised `List<Permission>`.




This fix will break code that relied on casting the List or its contents to `List<Map>`. If you have used this method in any capacity, you are likely to have done this and be affected.





### IDs are no longer set when exporting authorization settings for a client



When exporting the authorization settings for a client, the IDs for resources, scopes, and policies are no longer set. As a
result, you can now import the settings from a client to another client.





### Management port for metrics and health endpoints



Metrics and health checks endpoints are no longer accessible through the standard Keycloak server port.
As these endpoints should be hidden from the outside world, they can be accessed on a separate default management port `9000`.




It allows to not expose it to the users as standard Keycloak endpoints in Kubernetes environments.
The new management interface provides a new set of options and is fully configurable.




Keycloak Operator assumes the management interface is turned on by default.
For more details, see [Configuring the Management Interface](https://www.keycloak.org/server/management-interface).





### Syslog for remote logging



Keycloak now supports [Syslog](https://en.wikipedia.org/wiki/Syslog) protocol for remote logging.
It utilizes the protocol defined in [RFC 5424](https://datatracker.ietf.org/doc/html/rfc5424).
By default, the syslog handler is disabled, but when enabled, it sends all log events to a remote syslog server.




For more information, see the [Configuring logging](https://www.keycloak.org/server/logging) guide.





### Change to class `EnvironmentDependentProviderFactory`



The method `EnvironmentDependentProviderFactory.isSupported()` was deprecated for several releases and has now been removed.




For more details, see the [Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/).





### All `cache` options are runtime



It is now possible to specify the `cache`, `cache-stack`, and `cache-config-file` options during runtime.
This eliminates the need to execute the build phase and rebuild your image due to them.




For more details, see the [Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/).





### High availability guide enhanced



The high availability guide now contains a guide on how to configure an AWS Lambda to prevent an intended automatic failback from the Backup site to the Primary site.





### Removing deprecated methods from `AccessToken`, `IDToken`, and `JsonWebToken` classes



In this release, we are finally removing deprecated methods from the following classes:




* `AccessToken`
* `IDToken`
* `JsonWebToken`




For more details, see the [Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/).





### Method `getExp` added to `SingleUseObjectKeyModel`



As a consequence of the removal of deprecated methods from `AccessToken`, `IDToken`, and `JsonWebToken`,
the `SingleUseObjectKeyModel` also changed to keep consistency with the method names related to expiration values.




For more details, see the [Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/).





### Support for PostgreSQL 16



The supported and tested databases now include PostgreSQL 16\.





### Introducing support for Customer Identity and Access Management (CIAM) and Multi\-tenancy



In this release, we are delivering Keycloak Organizations as a technology preview feature.




This feature provides a realm with some core CIAM capabilities, which will serve as the baseline for more capabilities
in the future to address Business\-to\-Business (B2B) and Business\-to\-Business\-to\-Customers (B2B2C) use cases.




In terms of functionality, the feature is completed. However, we still have work to do to make it fully supported in the next major release.
This remaining work is mainly about preparing the feature for production deployments with a focus on scalability. Also, depending
on the feedback we get until the next major release, we might eventually accept additional capabilities and add more value to
the feature, without compromising its roadmap.




For more details, see [Server Administration Guide](https://www.keycloak.org/docs/25.0.6/server_admin/#_managing_organizations).







Keycloak 24\.0\.5
-----------------




### Security issue with PAR clients using client\_secret\_post based authentication



This release contains the fix of the important security issue affecting some OIDC confidential clients using PAR (Pushed authorization request). In case you use OIDC confidential clients together
with PAR and you use client authentication based on `client_id` and `client_secret` sent as parameters in the HTTP request body (method `client_secret_post` specified in the OIDC specification), it is
highly encouraged to rotate the client secrets of your clients after upgrading to this version.







Keycloak 24\.0\.4
-----------------




### Partial update to user attributes when updating users through the Admin User API is no longer supported



When updating user attributes through the Admin User API, you cannot execute partial updates when updating the
user attributes, including the root attributes like `username`, `email`, `firstName`, and `lastName`.




For more details, see the [Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/).







Keycloak 24\.0\.1
-----------------




### Operator deploys nightly build instead of 24\.0\.0



Due to an issue in the release process when deploying Keycloak using the Operator it installed the `nightly` container
instead of `24.0.0`.




As a quick fix to the issue, the `24.0.0` container was tagged with `nightly`, and the `nightly` releases was temporarily
disabled.




If you installed or upgraded to `24.0.0` using the Operator before 5pm CET yesterday the database may have been updated
with the wrong versions. To check if you are affected connect to your database and run the following SQL command:






```
SELECT * from migration_model WHERE version = '999.0.0';
```




If the above returns a matching row you will need to take some actions, otherwise database migrations will not run for
future releases. To resolve this run the following SQL command:






```
UPDATE migration_model SET version = '24.0.0' WHERE version = '999.0.0';
```







Keycloak 24\.0\.0
-----------------




### Supported user profile and progressive profiling



The user profile preview feature is promoted to be fully supported and user profile is enabled by default.




In the past months, the Keycloak team spent a huge amount of effort in polishing the user
profile feature to make it fully supported. In this release, we continued the effort. Lots of improvements, fixes and
polishing were done based on the thorough testing and feedback from our awesome community.




The following are a few highlights of this feature;




* Fine\-grained control over the attributes that users and administrators can manage so that you can prevent unexpected attributes and values from being set.
* Ability to specify what user attributes are managed and should be displayed on the forms to regular users or administrators.
* Dynamic forms \- Previously, the forms where users created or updated their profiles, contain four basic attributes like username, email, first name and last name. The addition of any
attributes (or removing some default attributes) required you to create a custom theme. Now custom themes may not be needed because users see exactly the requested attributes based on the requirement of the particular deployment.
* Validations \- Ability to specify validators for the user attributes including built\-in validators that you can use to specify a maximum or minimum length, a specific regex, or limiting a
particular attribute to be a URL or number.
* Annotations \- Ability to specify that particular attribute should be rendered for instance as a text area, an HTML select with specified options, or calendar or many other options. You can also bind JavaScript code to a specific field to change how an attribute is rendered and customize its behavior.
* Progressive profiling \- Ability to specify that some fields are required or available on the forms just for particular values of `scope` parameter. This effectively allow progressive
profiling. You no longer need to ask the user for twenty attributes during registration; you can instead ask the user to fill in attributes incrementally according to the requirements of the individual client
applications that are used by the user.
* Migration from previous versions \- The user profile is now always enabled, but it operates as before for those who did not use this feature. You can
benefit from the user profile capabilities, but you are not required to use them. For migration instructions, see the [Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/).




The first release of the user profile as a supported feature is just the starting point and the baseline for delivering many more capabilities around identity management.




We would like to give huge thanks to the awesome Keycloak community as lots of ideas, requirements and contributions came from the community! Special thanks to:




* [Vlastimil Eliáš](https://github.com/velias)
* [Alec Henninger](https://github.com/alechenninger)
* [Thomas Darimont](https://github.com/thomasdarimont)
* [Markus Till](https://github.com/bs-matil)
* [Sebastian Schuster](https://github.com/sschu)
* [Oliver](https://github.com/antikalk)
* [Patrick Jennings](https://github.com/patrickjennings)
* [Andrew](https://github.com/adrhine)




For more details about user profile capabilities, see the [Server Administration Guide](https://www.keycloak.org/docs/25.0.6/server_admin/#user-profile).




#### Breaking changes to the User Profile SPI



In this release, changes to the User Profile SPI might impact existing implementations based on this SPI. For more details, see the
[Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/).





#### Changes to Freemarker templates to render pages based on the user profile and realm



In this release, the following templates were updated to make it possible to dynamically render attributes based
on the user profile configuration set to a realm:




* `login-update-profile.ftl`
* `register.ftl`
* `update-email.ftl`




For more details, see the [Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/).





#### New Freemarker template for the update profile page at first login through a broker



In this release, the server renders the update profile page when the user is authenticating through a broker for the
first time using the `idp-review-user-profile.ftl` template.




For more details, see the [Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/).






### Java adapter deprecation and removal



Back in 2022 we announced the [deprecation of Keycloak adapters in Keycloak 19](https://www.keycloak.org/2022/02/adapter-deprecation.html).
To give the community more time to adopt this [was delayed](https://www.keycloak.org/2023/03/adapter-deprecation-update.html).




With that in mind, this will be the last major release of Keycloak to include OpenID Connect and SAML adapters.
As Jetty 9\.x has not been supported since 2022 the Jetty adapter has been removed already in this release.




The generic Authorization Client library will continue to be supported, and aims to be used in combination with any
other OAuth 2\.0 or OpenID Connect libraries.




The only adapter we will continue to deliver is the SAML adapter for latest releases of WildFly and EAP 8\.x. Reasoning
for continuing to support this is down to the fact that the majority of the SAML codebase in Keycloak was a contribution
from WildFly. As part of this contribution we agreed to maintain SAML adapters for WildFly and EAP in the long run.




#### Jetty adapter removed



Jetty 9\.4 has not been supported in the community for a long time, and reached end\-of\-life in 2022\. At the same time the
adapter has not been updated or tested with more recent versions of Jetty. For these reasons the Jetty adapter has been
removed from this release.






### New Welcome Page



The 'welcome' page that appears at the first use of Keycloak is redesigned. It provides a better setup experience and conforms to the latest version of [PatternFly](https://www.patternfly.org/). The simplified page layout includes only a form to register the first administrative user. After completing the registration, the user is sent directly to the Admin Console.




If you use a custom theme, you may need to update it to support the new welcome page. For details, see the [Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/).





### New Account Console now the default



We introduced version 3 of the Account Console in Keycloak 22 as a preview feature. In this release, we are making it the default version, and deprecating version 2 in the process, which will be removed in a subsequent release.




This new version has built\-in support for the user profile feature, which allows administrators to configure which attributes are available to users in the Account Console, and lands a user directly on their personal account page after logging in.




If you are using or extending the customization features of this theme, you may need to perform additional migrations. For more details, see the [Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/).





### Keycloak JS



#### Using `exports` field in `package.json`



The Keycloak JS adapter now uses the [`exports` field](https://webpack.js.org/guides/package-exports/) in its `package.json`. This change improves support for more modern bundlers like Webpack 5 and Vite, but comes with some unavoidable breaking changes. See the [Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/) for more details.





#### PKCE enabled by default



The Keycloak JS adapter now sets the `pkceMethod` option to `S256` by default. This change enables Proof Key Code Exchange ([PKCE](https://datatracker.ietf.org/doc/html/rfc7636)) for all applications using the adapter. If you use the adapter on a system that does not support PKCE, you can set the `pkceMethod` option to `false` to disable it.






### Changes to Password Hashing



In this release, we adapted the password hashing defaults to match the [OWASP recommendations for Password Storage](https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html#pbkdf2).




As part of this change, the default password hashing provider has changed from `pbkdf2-sha256` to `pbkdf2-sha512`.
Also, the number of default hash iterations for `pbkdf2` based password hashing algorithms changed. This change means better security aligned with latest recommendations, but
it has impact on performance. It is possible to stick to the old behaviour by adding password policies `hashAlgorithm` and `hashIterations` to your realm. For more details, see the [Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/).





### OAuth/OIDC related improvements



#### Lightweight access tokens support



This release contains support for Lightweight access tokens. As a result, you can have smaller access tokens for specified clients. These tokens have only a few
claims, which is why they are smaller. Note that lightweight access token is still JWT signed by the realm key by default and still contains some very basic claims.




This release introduces an **Add to lightweight access token** flag that is available on some OIDC protocol mappers. Use this flag to specify if a particular claim should be added to a lightweight
access token. It is **OFF** by default, which means that most claims are not added.




Also, a client policy executor exists. Use it to specify if a particular client request
should use lightweight access tokens or regular access tokens. An alternative to the executor is to use an **Always use lightweight access token** flag on client advanced
settings, which causes that client to always use lightweight access tokens. An executor can be an alternative if you need
more flexibility. For instance, you may choose to use lightweight access tokens by default but use regular tokens only for the specified **scope** parameter.




A previous release added an **Add to token introspection** switch. You use it to add
claims that are not present in the access token into the introspection endpoint response.




Thanks to [Shigeyuki Kabano](https://github.com/skabano) for the contribution and Thanks to
[Takashi Norimatsu](https://github.com/tnorimat) for a help and review of this feature.





#### OAuth 2\.1 support



This release contains optional OAuth 2\.1 support. New client policy profiles were introduced in this release, which administrators can use to make sure that clients and particular client requests comply with the OAuth 2\.1 specification. A dedicated client profile exists for confidential clients and a dedicated profile for public clients.
Thanks to [Takashi Norimatsu](https://github.com/tnorimat) and [Shigeyuki Kabano](https://github.com/skabano) for the contribution.





#### Scope parameter supported in the refresh token flow



Starting with this release, the **scope** parameter in the OAuth2/OIDC endpoint for token refresh is supported. Use this parameter to request access tokens with a smaller amount
of scopes than originally granted, which means you cannot increase access token scope. This scope limitation does not affect the scope of the refreshed refresh token. This function works as
described in the OAuth2 specification.
Thanks to [Konstantinos Georgilakis](https://github.com/cgeorgilakis) for the contribution.





#### Client policy executor for secure redirect URIs



A new client policy executor `secure-redirect-uris-enforcer` is introduced. Use it to restrict which redirect URIs can be used by the clients. For instance,
you can specify that client redirect URIs cannot have wildcards, should be just from specific domain, must be OAuth 2\.1 compliant, and so on.
Thanks to [Lex Cao](https://github.com/lexcao) and [Takashi Norimatsu](https://github.com/tnorimat) for the contribution.





#### Client policy executor for enforcing DPoP



A new client policy executor `dpop-bind-enforcer` is introduced. You can use it to enforce DPoP for a particular client if `dpop` preview
 is enabled.
Thanks to [Takashi Norimatsu](https://github.com/tnorimat) for the contribution.





#### Supporting EdDSA



You can create EdDSA realm keys and use them as signature algorithms for various clients. For instance, you can use these keys to sign tokens or for client authentication with signed JWT.
This feature includes identity brokering where Keycloak itself signs client assertions that are used for `private_key_jwt` authentication to third party identity providers.
Thanks to
[Takashi Norimatsu](https://github.com/tnorimat) and [Muhammad Zakwan Bin Mohd Zahid](https://github.com/MuhammadZakwan) for the contribution.





#### EC Keys supported by JavaKeystore provider



The provider `JavaKeystoreProvider` for providing realm keys now supports EC keys in addition to previously supported RSA keys.
Thanks to [Stefan Wiedemann](https://github.com/wistefan) for the contribution.





#### Option to add X509 thumbprint to JWT when using private\_key\_jwt authentication for identity providers



OIDC identity providers now have the **Add X.509 Headers to the JWT** option for the situation when client authentication with JWT signed by private key is used. This option can be useful
for interoperability with some identity providers such as Azure AD, which require the thumbprint to be present on the JWT.
Thanks to [MT](https://github.com/MikeTangoEcho) for the contribution.





#### OAuth Grant Type SPI



The Keycloak codebase includes an internal update to introduce the OAuth Grant Type SPI. This update allows additional flexibility when introducing custom grant types
supported by the Keycloak OAuth 2 token endpoint.
Thanks to [Dmitry Telegin](https://github.com/dteleguin) for the contribution.






### CORS improvements



The CORS related Keycloak functionality was extracted into the SPI, which can allow additional flexibility. Note that `CorsSPI` is internal and may change at a future release.
Thanks to [Dmitry Telegin](https://github.com/dteleguin) for the contribution.





### Truststore improvements



Keycloak introduces improved truststores configuration options. The Keycloak truststore is now used across the server, including outgoing connections, mTLS, and database drivers. You no longer need to configure separate truststores for individual areas. To configure the truststore, you can put your truststores files or certificates in the default `conf/truststores`, or use the new `truststore-paths` config option. For details refer to the relevant [guide](https://www.keycloak.org/server/keycloak-truststore).





### Versioned Features



Features now support versioning. To preserve backward compatibility, all existing features (including `account2` and `account3`) are marked as version 1\. Newly introduced features will use versioning, which means that users can select between different implementations of desired features.




For details refer to the [features guide](https://www.keycloak.org/server/features).




#### Keycloak CR Truststores



You may also take advantage of the new server\-side handling of truststores by using the Keycloak CR, for example:






```
spec:
  truststores:
    mystore:
      secret:
        name: mystore-secret
    myotherstore:
      secret:
        name: myotherstore-secret
```




Currently only Secrets are supported.





#### Trust Kubernetes CA



The cert for the Kubernetes CA is added automatically to your Keycloak Pods managed by the Operator.






### Automatic certificate management for SAML identity providers



The SAML identity providers can now be configured to automatically download the signing certificates from the IDP entity metadata descriptor endpoint. In order to use the new feature, configure the `Metadata descriptor URL` option in the provider (the URL where the IDP metadata information with the certificates is published) and set `Use metadata descriptor URL` to `ON`. The certificates are automatically downloaded and cached in the `public-key-storage` SPI from that URL. The certificates can also be reloaded or imported from the Admin Console, using the action combo in the provider page.




See the [documentation](https://www.keycloak.org/docs/latest/server_admin/index.html#saml-v2-0-identity-providers) for more details about the new options.





### Non\-blocking health check for load balancers



A new health check endpoint available at `/lb-check` was added.
The execution is running in the event loop, which means this check is responsive also in overloaded situations when Keycloak needs to handle many requests waiting in request queue.
This behavior is useful, for example, in multi\-site deployment to avoid failing over to another site that is under heavy load.
The endpoint is currently checking availability of the embedded and external Infinispan caches. Other checks may be added later.




This endpoint is not available by default.
To enable it, run Keyloak with the `multi-site` feature.
For more details, see [Enabling and disabling features](https://www.keycloak.org/server/features).





### Keycloak CR Optimized Field



The Keycloak CR now includes an `startOptimized` field, which may be used to override the default assumption about whether to use the `--optimized` flag for the start command.
As a result, you can use the CR to configure build time options also when a custom Keycloak image is used.





### Enhanced reverse proxy settings



It is now possible to separately enable parsing of either `Forwarded` or `X-Forwarded-*` headers by using the new `--proxy-headers` option.
For details, see the [Reverse Proxy Guide](https://www.keycloak.org/server/reverseproxy).
The original `--proxy` option is now deprecated and will be removed in a future release. For migration instructions, see the [Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/).





### Changes to the user representation in both Admin API and Account contexts



In this release, we are encapsulating the root user attributes (such as `username`, `email`, `firstName`, `lastName`, and `locale`) by moving them to a base/abstract class in order to align how these attributes
are marshalled and unmarshalled when using both Admin and Account REST APIs.




This strategy provides consistency in how attributes are managed by clients and makes sure they conform to the user profile
configuration set to a realm.




For more details, see the [Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/).





### Sequential loading of offline sessions and remote sessions



Starting with this release, the first member of a Keycloak cluster will load remote sessions sequentially instead of in parallel.
If offline session preloading is enabled, those will be loaded sequentially as well.




For more details, see the [Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/).





### Performing actions on behalf of another already authenticated user is not longer possible



In this release, you can no longer perform actions such as email verification if the user is already authenticated
and the action is bound to another user. For instance, a user can not complete the verification email flow if the email link
is bound to a different account.





### Changes to the email verification flow



In this release, if a user tries to follow the link to verify the email and the email was previously verified, a proper message
will be shown.




In addition to that, a new error (`EMAIL_ALREADY_VERIFIED`) event will be fired to indicate an attempt to verify an already verified email. You can
use this event to track possible attempts to hijack user accounts in case the link has leaked or to alert users if they do not recognize the action.





### Deprecated offline session preloading



The default behavior of Keycloak is to load offline sessions on demand.
The old behavior to preload them at startup is now deprecated, as pre\-loading them at startup does not scale well with a growing number of sessions, and increases Keycloak memory usage. The old behavior will be removed in a future release.




For more details, see the
[Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/).





### Configuration option for offline session lifespan override in memory



To reduce memory requirements, we introduced a configuration option to shorten lifespan for offline sessions imported into the Infinispan caches. Currently, the offline session lifespan override is disabled by default.




For more details, see the
[Server Administration Guide](https://www.keycloak.org/docs/25.0.6/server_admin/#_offline-access).





### Infinispan metrics use labels for cache manager and cache names



When enabling metrics for Keycloak’s embedded caches, the metrics now use labels for the cache manager and the cache names.




For more details, see the
[Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/).





### User attribute value length extension



As of this release, Keycloak supports storing and searching by user attribute values longer than 255 characters, which was previously a limitation.




For more details, see the
[Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/).





### Brute Force Protection changes



There have been a couple of enhancements to the Brute Protection:




1. When an attempt to authenticate with an OTP or Recovery Code fails due to Brute Force Protection the active Authentication Session is invalidated. Any further attempts to authenticate with that session will fail.
2. In previous versions of Keycloak, the administrator had to choose between disabling users temporarily or permanently due to a Brute Force attack on their accounts. The administrator can now permanently disable a user after a given number of temporary lockouts.
3. The property `failedLoginNotBefore` has been added to the `brute-force/users/{userId}` endpoint





### Authorization Policy



In previous versions of Keycloak, when the last member of a User, Group or Client policy was deleted then that policy would also be deleted. Unfortunately this could lead to an escalation of privileges if the policy was used in an aggregate policy. To avoid privilege escalation the effect policies are no longer deleted and an administrator will need to update those policies.





### Keycloak CR cache\-config\-file option



The Keycloak CR now allows for specifying the `cache-config-file` option by using the `cache` spec `configMapFile` field, for example:






```
apiVersion: k8s.keycloak.org/v2alpha1
kind: Keycloak
metadata:
  name: example-kc
spec:
  ...
  cache:
    configMapFile:
      name: my-configmap
      key: config.xml
```





### Keycloak CR resources options



The Keycloak CR now allows for specifying the `resources` options for managing compute resources for the Keycloak container.
It provides the ability to request and limit resources independently for the main Keycloak deployment via the Keycloak CR, and for the realm import Job via the Realm Import CR.




When no values are specified, the default `requests` memory is set to `1700MiB`, and the `limits` memory is set to `2GiB`.




You can specify your custom values based on your requirements as follows:






```
apiVersion: k8s.keycloak.org/v2alpha1
kind: Keycloak
metadata:
  name: example-kc
spec:
  ...
  resources:
    requests:
      cpu: 1200m
      memory: 896Mi
    limits:
      cpu: 6
      memory: 3Gi
```




For more details, see the
[Operator Advanced configuration](https://www.keycloak.org/operator/advanced-configuration).





### Temporary lockout log replaced with event



There is now a new event `USER_DISABLED_BY_TEMPORARY_LOCKOUT` when a user is temporarily locked out by the brute force protector.
The log with ID `KC-SERVICES0053` has been removed as the new event offers the information in a structured form.




For more details, see the
[Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/).





### Updates to cookies



Cookie handling code has been refactored and improved, including a new Cookie Provider. This provides better consistency
for cookies handled by Keycloak, and the ability to introduce configuration options around cookies if needed.





### SAML User Attribute Mapper For NameID now suggests only valid NameID formats



User Attribute Mapper For NameID allowed setting `Name ID Format` option to the following values:




* `urn:oasis:names:tc:SAML:1.1:nameid-format:X509SubjectName`
* `urn:oasis:names:tc:SAML:1.1:nameid-format:WindowsDomainQualifiedName`
* `urn:oasis:names:tc:SAML:2.0:nameid-format:kerberos`
* `urn:oasis:names:tc:SAML:2.0:nameid-format:entity`




However, Keycloak does not support receiving `AuthnRequest` document with one of these `NameIDPolicy`, therefore these
mappers would never be used. The supported options were updated to only include the following Name ID Formats:




* `urn:oasis:names:tc:SAML:1.1:nameid-format:emailAddress`
* `urn:oasis:names:tc:SAML:1.1:nameid-format:unspecified`
* `urn:oasis:names:tc:SAML:2.0:nameid-format:persistent`
* `urn:oasis:names:tc:SAML:2.0:nameid-format:transient`





### Different JVM memory settings when running in a container



Instead of specifying hardcoded values for the initial and maximum heap size, Keycloak uses relative values to the total memory of a container.
The JVM options `-Xms` and `-Xmx` were replaced by `-XX:InitialRAMPercentage` and `-XX:MaxRAMPercentage`.






|  | It can significantly impact memory consumption, so executing particular actions might be required. |
| --- | --- |




For more details, see the [Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/).





### GELF log handler has been deprecated



With sunsetting of the [underlying library](https://github.com/mp911de/logstash-gelf) providing integration
with GELF, Keycloak will no longer support the GELF log handler out\-of\-the\-box. This feature will be removed in a future
release. If you require an external log management, consider using file log parsing.





### Support for multi\-site active\-passive deployments



Deploying Keycloak to multiple independent sites is essential for some environments to provide high availability and a speedy recovery from failures.
This release supports active\-passive deployments for Keycloak.




To get started, use the [High Availability Guide](https://www.keycloak.org/guides#high-availability) which also includes a comprehensive blueprint to deploy a highly available Keycloak to a cloud environment.







Keycloak 23\.0\.0
-----------------




### OpenID Connect / OAuth 2\.0



#### FAPI 2 drafts support



Keycloak has new client profiles `fapi-2-security-profile` and `fapi-2-message-signing`, which ensure Keycloak enforces compliance with
the latest FAPI 2 draft specifications when communicating with your clients.
Thanks to [Takashi Norimatsu](https://github.com/tnorimat) for the contribution.





#### DPoP preview support



Keycloak has preview for support for OAuth 2\.0 Demonstrating Proof\-of\-Possession at the Application Layer (DPoP).
Thanks to
[Takashi Norimatsu](https://github.com/tnorimat) and [Dmitry Telegin](https://github.com/dteleguin) for their contributions.





#### More flexibility for introspection endpoint



In previous versions, introspection endpoint automatically returned most claims, which were available in the access token. Now most of protocol mappers include a new
 `Add to token introspection` switch . This addition allows more flexibility because an introspection endpoint can return different
claims than an access token. This change is a first step towards "Lightweight access tokens" support because access tokens can omit lots of the claims, which would be still returned
by the introspection endpoint. When migrating from previous versions, the introspection endpoint should return same claims, which are returned from access token,
so the behavior should be effectively the same by default after the migration.
Thanks to [Shigeyuki Kabano](https://github.com/skabano) for the contribution.





#### Feature flag for OAuth 2\.0 device authorization grant flow



The OAuth 2\.0 device authorization grant flow now includes a feature flag, so you can easily disable this feature. This feature is still enabled by default.
Thanks to [Thomas Darimont](https://github.com/thomasdarimont) for the contribution.






### Authentication



#### Passkeys support



Keycloak has preview support for [Passkeys](https://fidoalliance.org/passkeys/).




Passkey registration and authentication are realized by the features of WebAuthn.
Therefore, users of Keycloak can do Passkey registration and authentication by existing WebAuthn registration and authentication.




Both synced Passkeys and device\-bound Passkeys can be used for both Same\-Device and Cross\-Device Authentication.
However, Passkeys operations success depends on the user’s environment. Make sure which operations can succeed in [the environment](https://passkeys.dev/device-support/).
Thanks to [Takashi Norimatsu](https://github.com/tnorimat) for the contribution and thanks to [Thomas Darimont](https://github.com/thomasdarimont) for the help with the
ideas and testing of this feature.





#### WebAuthn improvements



WebAuthn policy includes a new field: `Extra Origins`. It provides better interoperability with non\-Web platforms (for example, native mobile applications).
Thanks to [Charley Wu](https://github.com/akunzai) for the contribution.





#### You are already logged\-in



This release addresses an issue concerning when a user has a login page open in multiple browser tabs and authenticated in one browser tab. When the user tries to authenticate in another browser tab, a message appears: `You are already logged-in`. This is improved now as
other browser tabs automatically authenticate the user after authentication in the first tab. However, more improvements are still needed. For example, when an authentication session expires and is restarted in one browser tab, other browser tabs do not follow automatically with the login.





#### Password policy for specify Maximum authentication time



Keycloak supports a new password policy that allows you to specify the maximum age of an authentication with which a password may be changed by a user without re\-authentication.
When this password policy is set to 0, the user is required to re\-authenticate to change the password in the Account Console or by other means.
You can also specify a lower or higher value than the default value of 5 minutes.
Thanks to [Thomas Darimont](https://github.com/thomasdarimont) for the contribution.






### Deployments



#### Preview support for multi\-site active\-passive deployments



Deploying Keycloak to multiple independent sites is essential for some environments to provide high availability and a speedy recovery from failures.
This release adds preview\-support for active\-passive deployments for Keycloak.




A lot of work has gone into testing and verifying a setup which can sustain load and recover from the failure scenarios.
To get started, use the [High Availability Guide](https://www.keycloak.org/guides#high-availability) which also includes a comprehensive blueprint to deploy a highly available Keycloak to a cloud environment.






### Adapters



#### OpenID Connect WildFly and JBoss EAP



OpenID Connect adapter for WildFly and JBoss EAP, which was deprecated in previous versions, has been removed in this release.
It is being replaced by the Elytron OIDC adapter,which is included in WildFly, and provides a seamless migration from
Keycloak adapters.





#### SAML WildFly and JBoss EAP



The SAML adapter for WildFly and JBoss EAP is no longer distributed as a ZIP download, but rather a Galleon feature pack,
making it easier and more seamless to install.




See the [Securing Applications and Services Guide](https://www.keycloak.org/docs/25.0.6/securing_apps/) for the details.






### Server distribution



#### Load Shedding support



Keycloak now features `http-max-queued-requests` option to allow proper rejecting of incoming requests under high load.
For details refer to the [production guide](https://www.keycloak.org/server/configuration-production).





#### RESTEasy Reactive



Keycloak has switched to RESTEasy Reactive. Applications using `quarkus-resteasy-reactive` should still benefit from a better startup time, runtime performance, and memory footprint, even though not using reactive style/semantics. SPIs that depend directly on JAX\-RS API should be compatible with this change. SPIs that depend on RESTEasy Classic including `ResteasyClientBuilder` will not be compatible and will require an update. This update will also be needed for other implementation of the JAX\-RS API like Jersey.






### User profile



Declarative user profile is still a preview feature in this release, but we are working hard on promoting it to a supported feature. Feedback is welcome.
If you find any issues or have any improvements in mind, you are welcome to create [Github issue](https://github.com/keycloak/keycloak/issues/new/choose),
ideally with the label `area/user-profile`. It is also recommended to check the [Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/) with the migration changes for this
release for some additional information related to the migration.





### Group scalability



Performance around searching of groups is improved for the use\-cases with many groups and subgroups. There are improvements, which allow
paginated lookup of subgroups.
Thanks to [Alice](https://github.com/alice-wondered) for the contribution.





### Themes



#### Localization files for themes default to UTF\-8 encoding



Message properties files for themes are now read in UTF\-8 encoding, with an automatic fallback to ISO\-8859\-1 encoding.




See the migration guide for more details.






### Storage



#### Removal of the Map Store



The Map Store has been an experimental feature in previous releases.
Starting with this release, it is removed and users should continue to use the current JPA store.
See the migration guide for details.








Keycloak 22\.0\.3
-----------------




### Security vulnerability when registering or updating user through templates



A security vulnerability was introduced in Keycloak 22\.0\.2\. We highly recommend not upgrading to 22\.0\.2, and for anyone that has deployed 22\.0\.2 in production to upgrade to 22\.0\.3 immediately.




For users that has self\-registered after Keycloak was upgraded to 22\.0\.2 their password is not stored securely, and can be exposed to administrators of Keycloak. This only affects users that has registered after the upgrade was rolled\-out, and does not affect any previously registered users.




Any realm using the preview declarative user profile is not affected by this issue, and only realms using the default user profile provider is affected.




To identify if there are any affected users in your deployment you can query these by accessing the database, and running the following SQL statement:






```
SELECT DISTINCT U.ID, U.USERNAME, U.EMAIL, U.REALM_ID FROM USER_ENTITY U
    INNER JOIN USER_ATTRIBUTE UA ON U.ID = UA.USER_ID
    WHERE UA.NAME IN ('password','password-confirm')
```




We recommend contacting any affected users as well as adding the update password required action for them.




If there are any affected users we also recommend removing these attributes from the database by running the following SQL statement:






```
DELETE FROM USER_ATTRIBUTE UA WHERE UA.NAME IN ('password','password-confirm')
```




If any backups have been done of the database after the 22\.0\.2 release and there are affected users, we recommend deleting these.




#### Custom user storage providers



Any deployments with custom user storage federation providers may also be affected if the provider is delegating to Keycloak storing user attributes,
please verify your custom user storage to identify if this is an issue.




To identify if there are any federated user affected in your deployment, you can query these by accessing the database, and running the following SQL statement:






```
SELECT DISTINCT USER_ID,REALM_ID,STORAGE_PROVIDER_ID FROM FED_USER_ATTRIBUTE
    WHERE NAME IN ('password','password-confirm')
```




If there are any affected federated users, we also recommend removing these attributes from the database by running the following SQL statement:






```
DELETE FROM FED_USER_ATTRIBUTE UA WHERE UA.NAME IN ('password','password-confirm')
```




If your custom user storage provider is managing attributes itself, you should look at your custom storage to remove the `password` and `password-confirm` attributes.








Keycloak 22\.0\.2
-----------------




### Improvements in LDAP and Kerberos integration



Keycloak now supports multiple LDAP providers in a realm, which support Kerberos integration with the same Kerberos realm. When an LDAP provider is not able to find the user which was authenticated through
Kerberos/SPNEGO, Keycloak ties to fallback to the next LDAP provider. Keycloak has also better support for the case when single LDAP provider supports multiple Kerberos realms, which are in trust with each other.







Keycloak 22\.0\.0
-----------------




### Server Distribution



#### Java 11 support removed



Running the Keycloak server with Java 11 is no longer supported. Java 11 was deprecated in Keycloak 21 with the announced plan to be removed in Keycloak 22\.





#### Upgrade to Quarkus 3\.x



Keycloak upgraded to version 3\.2\.0\.Final of the Quarkus Java framework.
Quarkus 3\.x continues the tradition of propelling Java development by moving fast and providing a cutting\-edge user experience with the latest technologies.




##### Transition from Java EE to Jakarta EE



As part of upgrading to Quarkus 3\.x Keycloak migrated its codebase from Java EE (Enterprise Edition) to its successor Jakarta EE, which brings various changes into Keycloak.
We have upgraded all Jakarta EE specifications in order to support Jakarta EE 10\.





##### Context and dependency injection no longer enabled to JAX\-RS Resources



In order to provide a better runtime and leverage as much as possible the underlying stack,
all injection points for contextual data using the `javax.ws.rs.core.Context` annotation were removed. The expected improvement
in performance involves no longer creating proxies instances multiple times during the request lifecycle, and drastically reducing the amount of reflection code at runtime.






#### Upgrade to Hibernate ORM 6



Keycloak now benefits from the upgrade to Hibernate ORM 6\.2, which includes improved performance, better SQL, modern JDK support, and support for modern RDBMS features.





#### Elytron credential store replacement



The previous and now removed WildFly distribution provided a built\-in vault provider that reads secrets from a keystore\-backed Elytron credential store. As this is no longer available, we have added a new implementation of the Keycloak Vault SPI called Keycloak KeyStore Vault. As the name suggests, this implementation reads secrets from a Java keystore file. Such secrets can be then used within multiple places of the Administration Console. For further details, see [our guide](https://www.keycloak.org/server/vault) and the latest [documentation](https://www.keycloak.org/docs/latest/server_admin/index.html#_vault-administration).





#### KeyStore Config Source added



In relation to the KeyStore Vault news, we also integrated Quarkus’s recently released feature called KeyStore Config Source. This means that among the already existing configuration sources (CLI parameters, environment variables and files), you can now configure your Keycloak server via configuration properties stored in a Java keystore file. You can learn more about this feature in the [Configuration guide](https://www.keycloak.org/server/configuration).





#### Hostname debug tool



As a number of users have had problems with configuring the hostname for the server correctly there is now a new helper tool to allow debugging the configuration.





#### Passthrough proxy mode changes



Installations which use Keycloak’s `--proxy` configuration setting with mode **passthrough** should review the documentation as the behavior of this mode has changed.





#### Export and Import perform an automatic build



In previous releases, the `export` and `import` commands required a `build` command to be run first.
Starting with this release, the `export` and `import` commands perform an automatic rebuild of Keycloak if a build time configuration has changed.






### Admin Console



#### Account Console v1 removal



The old Account Console (v1\) is now completely removed. This version of the Account Console was marked as deprecated
in Keycloak 12\.





#### Account Console v3 promoted to preview



In version 21\.1\.0 of Keycloak the new Account Console (version 3\) was introduced as an experimental feature. Starting this version it has been promoted to a preview feature.





#### Account Console template variables removed



Two of the variables exposed to the Account Console V2 and V3 templates (`isEventsEnabled` and `isTotpConfigured`) were left unused, and have been removed in this release.




It is possible that if a developer extended the Account Console theme, he or she could make use of these variables. So make sure that these variables are no longer used if you are extending the base theme.





#### Changes to custom Admin Console messages



The Admin Console (and soon also the new Account Console) works slightly different than the rest of Keycloak in regards to how keys for internationalized messages are parsed. This is due to the fact that it uses the [i18next](https://www.i18next.com/) library for internationalization. Therefore when defining custom messages for the Admin Console under "Realm Settings" ➡ "Localization" best practices for i18next must be taken into account. Specifically, when defining a message for the Admin Console it is it important to specify a [namespace](https://www.i18next.com/principles/namespaces) in the key of your message.




For example, let’s assume we want to overwrite the [`welcome`](https://github.com/keycloak/keycloak/blob/025778fe9c745316f80b53fe3052aeb314e868ef/js/apps/admin-ui/public/locales/en/dashboard.json#L3) message shown to the user when a new realm has been created. This message is located in the `dashboard` namespace, same as the name of the original file that holds the messages (`dashboard.json`). If we wanted to overwrite this message we’ll have to use the namespace as a prefix followed by the key of the message separated by a colon, in this case it would become `dashboard:welcome`.






### JavaScript adapter



#### Legacy Promise API removed



With this release, we have removed the legacy Promise API methods from the Keycloak JS adapter. This means that calling `.success()` and `.error()` on promises returned from the adapter is no longer possible.





#### Required to be instantiated with the `new` operator



In a previous release we started to actively log deprecation warnings when the Keycloak JS adapter is constructed without the `new` operator. Starting this release doing so will throw an exception instead. This is to align with the expected behavior of [JavaScript classes](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Classes), which will allow further refactoring of the adapter in the future.






### Admin API



#### Renamed Admin library artifacts



After the upgrade to Jakarta EE, artifacts for Keycloak Admin clients were renamed to more descriptive names with consideration for long\-term maintainability.
We still provide two separate Keycloak Admin clients, one with Jakarta EE and the other with Java EE support.





#### Support for count users based on custom attributes



The User API now supports querying the number of users based on custom attributes. For that, a new `q` parameter was added to the `/{realm}/users/count` endpoint.




The `q` parameter expects the following format `q=<name>:<value> <name>:<value>`. Where `<name>` and `<value>` represent the attribute name and value, respectively.






### Operator



#### k8s.keycloak.org/v2alpha1 changes



The are additional fields available in the keycloak.status to facilitate keycloak being a scalable resource. There are also additional fields that make the status easier to interpret such as observedGeneration and condition observedGeneration and lastTransitionTime fields.




The condition status field was changed from a boolean to a string for conformance with standard Kubernetes conditions. In the CRD it will temporarily be represented as accepting any content, but it will only ever be a string. Please make sure any of your usage of this field is updated to expect the values "True", "False", or "Unknown", rather than true or false.





#### Co\-management of Operator Resources



In scenarios where advanced management is needed you may now directly update most fields on operator managed resources that have not been set by the operator directly. This can be used as an alternative to the unsupported stanza of the Keycloak spec. Like the unsupported stanza these direct modifications are not considered supported. If your modifications prevent the operator from being able to manage the resource, there Keycloak CR will show this error condition and the operator will log it.






### Identity Brokering



#### Essential claim configuration in OpenID Connect identity providers



OpenID Connect identity providers support a new configuration to specify that the ID tokens issued by the identity provider must have a specific claim,
otherwise the user can not authenticate through this broker.




The option is disabled by default; when it is enabled, you can specify the name of the JWT token claim to filter and the value to match
(supports regular expression format).





#### Support for JWE encrypted ID Tokens and UserInfo responses in OpenID Connect providers



The OpenID Connect providers now support [Json Web Encryption (JWE)](https://datatracker.ietf.org/doc/html/rfc7516) for the ID Token and the UserInfo response. The providers use the realm keys defined for the selected encryption algorithm to perform the decryption.





#### Hardcoded group mapper



The new hardcorded group mapper allows adding a specific group to users brokered from an Identity Provider.





#### User session note mapper



The new user session note mapper allows mapping a claim to the user session notes.






### LDAP Federation



#### LDAPS\-only Truststore option removed



LDAP option to use truststore SPI `Only for ldaps` has been removed. This parameter is used to
select truststore for TLS\-secured LDAP connection: either internal Keycloak truststore is
picked (`Always`), or the global JVM one (`Never`).




Deployments where `Only for ldaps` was used will automatically behave as if `Always` option was
selected for TLS\-secured LDAP connections.






### Removed Openshift integration feature



The `openshift-integration` preview feature that allowed replacing the internal IdP in OpenShift 3\.x with Keycloak was removed from Keycloak codebase into separate extension project.







Keycloak 21\.1\.2
-----------------




### Changes in validating schemes for valid redirect URIs



If an application client is using non http(s) custom schemes, from now on the validation requires that a valid redirect pattern explicitly allows that scheme. Example patterns for allowing `custom` scheme are `custom:/test`, `custom:/test/*` or `custom:*`. For security reasons a general pattern like `*` does not cover them anymore.







Keycloak 21\.1\.0
-----------------




### Monorepo



In the past Keycloak was maintained across multiple GitHub repositories:




* [Documentation repository](https://github.com/keycloak/keycloak-documentation)
* [UI repository](https://github.com/keycloak/keycloak-ui)
* [Node.js admin client repository](https://github.com/keycloak/keycloak-nodejs-admin-client)




Having multiple repositories introduced a lot of complexity and toil. For example frequently multiple pull requests had to be sent
to different repositories for a single change.




To simplify things we have now migrated everything into the [main repository](https://github.com/keycloak/keycloak).





### FIPS 140\-2 support



FIPS 140\-2 support in Keycloak, which was preview in the previous release, is now promoted to be officially supported.





### Experimental Account Console version 3



The Account Console version 3 is now available as an experimental feature in Keycloak. This version supports custom fields created with the 'User Profile' feature. If you are looking to try it out and provide us with some early feedback you can enable it as follows:






```
bin/kc.sh start-dev --features=account3
```





### Changes to Keycloak Authorization Services support in Keycloak Java\-based Adapters



As part of the removal of the [deprecated](https://www.keycloak.org/2023/03/adapter-deprecation-update) adapters, the Keycloak Policy Enforcer was extracted from the adapters code base
into a separate dependency:






```
<dependency>
    <groupId>org.keycloak</groupId>
    <artifactId>keycloak-policy-enforcer</artifactId>
    <version>21.1.0</version>
</dependency>
```




By providing this dependency, we expect making it possible to integrate the policy enforcer with the Java stack of your preference.




It also provides built\-in support for enabling the policy enforcer to Jakarta applications protected with [Wildfly Elytron](https://docs.wildfly.org/26/Admin_Guide.html#Elytron_OIDC_Client).




For now, this dependency is not yet GA as we are still working on the quickstarts and documentation.




This work should not impact existing applications using the deprecated adapters.
\= Javascript engine available by default




In the previous version, when Keycloak was used on Java 17 with Javascript providers it was needed to add the Nashorn
javascript engine to the distribution. This is no longer needed as Nashorn javascript engine is available in Keycloak server by default.







Keycloak 21\.0\.0
-----------------




### Old Admin Console removed



In Keycloak 19 the new admin console was graduated to the new default admin console, and the old admin console was
deprecated. In this release the old admin console has been removed completely.





### Keycloak uses Micrometer for metrics



Keycloak provides an optional a metrics endpoint which exports metrics in the Prometheus format.
In this release the implementation to provide this data switched from SmallRye to Micrometer.
Due to this change, metrics have been renamed.




See the migration guide for details.





### Java 11 support for Keycloak server deprecated



Running the Keycloak server with Java 11 is now deprecated, and planned to be removed in Keycloak 22\.




Adapters remain supported on Java 8, Java 11, and Java 17\. However, we are planning to remove support for Java 8 in the
not too distant future.





### Hashicop Vault no longer supported



We removed the out\-of\-box support for Hashicorp vault in this release.




See this [discussion](https://github.com/keycloak/keycloak/discussions/16446) for more details.





### SAML SP metadata changes



Prior to this release, SAML SP metadata contained the same key for both
signing and encryption use. Starting with this version of Keycloak,
we include only encryption intended realm keys for encryption use
in SP metadata. For each encryption key descriptor we also specify
the algorithm that it is supposed to be used with. The following table shows
the supported XML\-Enc algorithms with the mapping to Keycloak realm keys.
See the [Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/) for more details.








| **XML\-Enc algorithm** | **Keycloak realm key algorithm** |
| --- | --- |
| [rsa\-oaep\-mgf1p](https://www.w3.org/TR/2002/REC-xmlenc-core-20021210/Overview.html#rsa-oaep-mgf1p) | RSA\-OAEP |
| [rsa\-1\_5](https://www.w3.org/TR/2002/REC-xmlenc-core-20021210/Overview.html#rsa-1_5) | RSA1\_5 |




### Deprecated methods from user session provider were removed



Several deprecated methods were removed from user session provider. If not done already,
their usage needs to be replaced with the corresponding replacement documented in Javadoc
of Keycloak 20 release. See [Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/) for more details.





### New storage: `IS_CLIENT_ROLE` searchable field was deprecated



The `IS_CLIENT_ROLE` searchable field from the `RoleModel` was deprecated. It
should be replaced with the `CLIENT_ID` searchable field used with the operators
`EXISTS` or `NOT_EXISTS`. See JavaDoc of Keycloak 21 for more details.





### FIPS 140\-2 preview support



FIPS 140\-2 support in Keycloak, which was experimental in the previous release, is now promoted to preview. There were many fixes and improvements to create this preview version.
For the details, see the [FIPS documentation](https://www.keycloak.org/server/fips). Feedback is welcome!




Thanks again to [David Anderson](https://github.com/david-rh), [Sudeep Das](https://github.com/sudeepd) and [Isaac Jensen](https://github.com/isaacjensen)
for their huge help with this feature.





### Support for the standard `Forwarded` header when running behind a reverse proxy



In addition to recognize the non\-standard `X-Forwarded-*` to fetch information
added by proxies that would otherwise be altered or lost when proxy servers are involved in the path of the request, Keycloak
can now leverage the standard `Forwarded` header for the same purpose.




For more details, see the [Using a reverse proxy](https://www.keycloak.org/server/reverseproxy) guide.




Please, make sure your proxy is also overriding the `Forwarded` header when making requests to Keycloak nodes.





### The container image is now based on ubi9\-micro



To enhance security, the [Keycloak Container Image](https://quay.io/repository/keycloak/keycloak?tab=info) has been modified in two ways: First, it is now based on UBI9, rather than UBI8\. Second, we have switched to `-micro`, whereas `-minimal` was used before.




The change to UBI9 will not have any impact on most users. In rare cases the glibc error [CPU does not support x86\-64\-v2](https://github.com/keycloak/keycloak/issues/17290) may appear. `x86-64-v2` has been available from processors since 2009\. You’re most likely to encounter this issue when your virtualization environment is misconfigured.




The change from `-minimal` to `-micro` has more potential impact. Users making simple customizations to the image won’t notice any difference, however any user that installs RPMs will need to change how they do that. The [Running Keycloak in a container](https://www.keycloak.org/server/containers) guide has been updated to show you how.




As a result of these changes, there has been an 82% reduction in known CVEs affecting the Keycloak Container Image!





### Other improvements



* Option to disable client registration access token rotation. Thanks to [Réda Housni Alaoui](https://github.com/reda-alaoui)







Keycloak 20\.0\.0
-----------------




### WildFly distribution removed



In Keycloak 17\.0\.0 the new Quarkus based distribution of Keycloak, while the WildFly based distribution was deprecated.
With this release the WildFly distribution has been removed, and is no longer supported.




If you are still using the WildFly distribution we highly encourage migrating to the Quarkus distribution as soon as
possible, see the [Migration Guide](https://www.keycloak.org/migration/migrating-to-quarkus) for more details.





### New Keycloak Operator upgrade



We are happy to announce that the new Keycloak Operator for the Quarkus based distribution is no longer a preview
feature. We added new functionality as well as a number of improvements, some which has resulted in breaking changes.




#### Realm Operator



As the new Operator currently lacks some of the CRs (e.g. Client and User), we’re introducing a temporary workaround in
the form of a Realm Operator. Please see its [GitHub Repository](https://github.com/keycloak/keycloak-realm-operator) for
more details. See also ["The future of Keycloak Operator CRs" blogpost](https://www.keycloak.org/2022/09/operator-crs).






### Supported OpenJDK versions



Keycloak now supports OpenJDK 17 both for the server and adapters.




With the removal of the WildFly based distribution there is no longer support for running the Keycloak server on OpenJDK 8\.
We also plan to remove support for Keycloak adapters on OpenJDK 8 in Keycloak 21\.




Starting with Keycloak 22 we plan to only support the latest OpenJDK LTS release and aiming to quickly also support the
latest OpenJDK release. That means we will be also removing OpenJDK 11 support for the Keycloak server in Keycloak 22\.





### Hostname provider now supports configuring the complete base URL



In this release, we are introducing two additional server options to set the base URL for frontend request and the Admin
Console:




* `hostname-url`
* `hostname-admin-url`




More details can be found at the [Configuring the Hostname](https://www.keycloak.org/server/hostname) guide.





### Improvements to `kc.bat` when running Keycloak on Windows



In this release, we are making important changes to `kc.bat` to give the same experience as when running on Linux.





### Upgrade of embedded H2 database



Keycloak ships for development purposes with an H2 database driver. As it is intended for development purposes
only, it should never be used in a production environment.




In this release, the H2 driver has been upgraded from version 1\.x to version 2\.x.





### Feature guard for hosting the Keycloak JavaScript adapter



Applications are able to load `keycloak.js` directly from the Keycloak server. As it’s not considered a best\-practice
to load JavaScript libraries this way there is now a feature guard that allows disabling this ability.




In Keycloak 21 we will deprecate this option, and in Keycloak 22 we plan to completely remove the ability to load
`keycloak.js` from the Keycloak server.





### OTP Application SPI



In previous releases the list of OTP applications displayed to users was hard\-coded in Keycloak. With the introduction of
the OTP Application SPI it is now possible to disable built\-in OTP applications, as well as adding custom OTP Applications.





### Custom Identity Providers can now set an icon for the provider



A custom identity provider can now set the icon used on the login pages. Thanks to [Klaus Betz](https://github.com/klausbetz),
who happens also to maintain
[an extension to Keycloak to support log in with AppleID](https://github.com/klausbetz/apple-identity-provider-keycloak).





### FIPS 140\-2 experimental support



There is now experimental support for deploying Keycloak into a FIPS 140\-2 enabled environment. There will be a blog post
with the details shortly after the release with the details how you can try it. Feedback is welcome!




Thanks to [David Anderson](https://github.com/david-rh), who contributed parts of this feature. Also, thanks to
[Sudeep Das](https://github.com/sudeepd) and [Isaac Jensen](https://github.com/isaacjensen) for their initial prototype
 effort, which was used as an inspiration.





### Search groups by attribute



It is now possible to search groups by attribute through the Admin REST API. Thanks to
[Alice](https://github.com/alice-wondered) for this contribution.





### View group membership in the account console



It is now possible to allow users to view their group memberships in the account console. Thanks to
[cgeorgilakis](https://github.com/cgeorgilakis) for this contribution.





### Deprecated methods from data providers and models were removed



Several deprecated methods were removed from data providers and models. If not done already, their usage needs to be
replaced with the corresponding replacement documented in Javadoc of Keycloak 19 release. See
[Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/) for more details.







Keycloak 19\.0\.0
-----------------




### OpenID Connect and SAML Adapters End\-of\-life



Some Keycloak OpenID Connect adapters have reached end\-of\-life and are not included in this release.




#### Fuse 6 and 7 (OpenID Connect)



Keycloak will no longer be providing adapters for Fuse 6 or 7\. If you need adapters for Fuse please leverage [Red Hat Single Sign\-On](https://access.redhat.com/products/red-hat-single-sign-on/) 7\.x adapters.





#### JBoss AS 7 and EAP 6 (OpenID Connect and SAML)



JBoss AS 7 has been unmaintained for a very long time. If you are still using JBoss AS 7 we recommend migrating to WildFly and leveraging the native OIDC support in WildFly.




Red Hat customers using Red Hat JBoss Enterprise Application Platform 6\.x should use [Red Hat Single Sign\-On](https://access.redhat.com/products/red-hat-single-sign-on/) 7\.x adapters. These can be used in combination with the Keycloak server.





#### Jetty 9\.2 and 9\.3 (OpenID Connect and SAML)



Jetty 9\.2 reached end of life in 2018, while Jetty 9\.3 reached end of life in 2020\. If you are still using these versions we recommend upgrading to Jetty 9\.4 as soon as possible.





#### Spring Boot 1 (OpenID Connect)



Spring Boot 1\.x reached end of life in 2019\. If you are still using Spring Boot 1 we recommend upgrading to Spring Boot 2 as soon as possible.





#### WildFly legacy security layer (OpenID Connect and SAML)



In WildFly 25 the legacy security layer was removed, going forward only Elytron will be supported. We recommend anyone using an older version of WildFly to upgrade and leverage native OIDC support in WildFly.




Red Hat customers using Red Hat JBoss Enterprise Application Platform 7\.x should use [Red Hat Single Sign\-On](https://access.redhat.com/products/red-hat-single-sign-on/) 7\.x adapters. These can be used in combination with the Keycloak server.






### New Admin Console graduation



The new Admin Console is now graduated to the default admin console, with the old console now deprecated. The old console will be removed in Keycloak 21\.





### Changes in Keycloak storage



The Keycloak storage is changing, and the current storage, while still supported, will eventually be replaced with a brand\-new implementation.
This change brings better support for cloud\-native storages, no\-downtime abilities, and better support for implementing custom storages for additional areas apart from users.




It means several deep changes in the supported features of the current store will become *legacy* features.
The legacy store and the new store cannot be used simultaneously; only one store can be active at a time.




The most visible change is that the User Storage SPI is incompatible with the new storage API, the Map Storage API.
Thus, the User Storage SPI will be deprecated with legacy store and will move to a separate module called `keycloak-model-legacy`.
This change impacts several areas, especially areas related to user federation and custom user providers.




Furthermore, APIs have been consolidated so that the details of the storage layer will be transparent to the REST service layer.
Specifically, the services will not be able to differentiate cached and non\-cached objects, nor specifically access federated versus local storage.




Hence, custom extensions that access objects in local storage or cache through `KeycloakSession`
methods must be reviewed.
See [Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/) for details.





### OIDC Logout changes



In the previous release, we added support for OIDC logout. This release contains a few other fixes and polishing. The highlights include:




* Support for the `client_id` parameter, which was added in recent draft of the OIDC RP\-Initiated Logout specification. As a result, no need exists to use the `Consent Required` flag of the
client to show the logout confirmation screen.
* Configuration option `Valid Post Logout Redirect URIs` added to the OIDC client. This change is aligned with the OIDC specification, which allows you to use a different set of redirect URIs for redirect after login and logout.
Value `+` used for `Valid Post Logout Redirect URIs` means that the logout will use the same set of redirect URIs as specified by the option of `Valid Redirect URIs`. This change also matches the default behavior when migrating
from a previous version due to backwards compatibility.




For more details, see the [Server Administration Guide](https://www.keycloak.org/docs/25.0.6/server_admin/#_oidc-logout).





### Update Email Workflow



There is new preview feature `UPDATE_EMAIL`. When it is enabled and corresponding flag enabled in the realm, the users will be required
to confirm updating their email by clicking the link, which will be sent to their new email address. For more details, see the [Server Administration Guide](https://www.keycloak.org/docs/25.0.6/server_admin/#_update-email-workflow).
Thanks to [Réda Housni Alaoui](https://github.com/reda-alaoui) for the contribution.





### Deprecated `podDisruptionBudget` in the legacy Keycloak Operator



With this release, we have deprecated `podDisruptionBudget` field in the Keycloak CR of the [legacy Keycloak Operator](https://github.com/keycloak/keycloak-operator).
This optional field will be ignored when the Operator is deployed on Kubernetes version 1\.25 and higher.




As a workaround, you can manually create the Pod Disruption Budget in your cluster, for example:






```
apiVersion: policy/v1
kind: PodDisruptionBudget
metadata:
  labels:
    app: keycloak
  name: keycloak
spec:
  maxUnavailable: 1
  selector:
    matchLabels:
      component: keycloak
```




See also the [Kubernetes Documentation](https://kubernetes.io/docs/tasks/run-application/configure-pdb/).





### Initial Support for centralized logging



Starting with version 19, Keycloak supports sending logs using GELF to centralized logging solutions like ELK, EFK or Graylog out of the box.




You can find the documentation and examples to get you up and running quickly in the [logging](https://www.keycloak.org/server/logging#_centralized_logging_using_gelf) guide.







Keycloak 18\.0\.0
-----------------




### New Operator preview



With this release, we’re introducing a brand new Keycloak Operator as a preview. Apart from being rewritten from
scratch, the main user\-facing change from the legacy Operator is the used Keycloak distribution – the new Operator
uses the Quarkus distribution of Keycloak. With that, the API (in form of Custom Resource Definitions) has changed.
For details, incl. installation and migration instructions, see the [Operator related guides](https://www.keycloak.org/guides#operator).




The [legacy Operator](https://github.com/keycloak/keycloak-operator) will receive updates until Keycloak 20 when the Keycloak WildFly
distribution reaches EOL.




#### OperatorHub versioning scheme



To avoid version conflicts with the legacy Operator, the 18\.0\.0 version of the new Operator is released as version
`20.0.0-alpha.1` on OperatorHub. The legacy Operator versioning scheme remains the same, i.e. it is released as 18\.0\.0\.




The same pattern will apply for future Keycloak 18 and 19 releases, until version 20 where the legacy Operator
reaches EOL.






### New Admin Console preview



The new Admin Console is now graduated to preview, with the plan for it to become the default admin console in Keycloak 19\.




If you find any issues with the new console, or have some suggestions for improvements, please let us know through [GitHub Discussions](https://github.com/keycloak/keycloak/discussions/categories/new-admin-console).





### Step\-up authentication



Keycloak now supports Step\-up authentication. This feature was added in Keycloak 17, and was further polished in this version.




For more details, see [Server Administration Guide](https://www.keycloak.org/docs/25.0.6/server_admin/#_step-up-flow).




Thanks to [Cornelia Lahnsteiner](https://github.com/CorneliaLahnsteiner) and [Georg Romstorfer](https://github.com/romge) for the contribution.





### Client secret rotation



Keycloak now supports Client Secret Rotation through customer policies. This feature is now available as a preview feature and allows that confidential clients can be provided with realm policies allowing the use up to two secrets simultaneously.




For more details, see [Server Administration Guide](https://www.keycloak.org/docs/25.0.6/server_admin/#_secret_rotation).





### Recovery Codes



Recovery Codes as another way to do two\-factor authentication is now available as a preview feature.





### OpenID Connect Logout Improvements



Some fixes and improvements were made to make sure that Keycloak is now fully compliant with all the OpenID Connect logout specifications:




* OpenID Connect RP\-Initiated Logout 1\.0
* OpenID Connect Front\-Channel Logout 1\.0
* OpenID Connect Back\-Channel Logout 1\.0
* OpenID Connect Session Management 1\.0




For more details, see [Server Administration Guide](https://www.keycloak.org/docs/25.0.6/server_admin/#_oidc-logout).





### WebAuthn improvements



Keycloak now supports WebAuthn id\-less authentication. This feature allows that WebAuthn Security Key will identify the user during authentication as long as the
security key supports Resident Keys. For more details, see [Server Administration Guide](https://www.keycloak.org/docs/25.0.6/server_admin/#_webauthn_loginless).
Thanks to [Joaquim Fellmann](https://github.com/vanrar68) for the contribution.




There are more WebAuthn improvements and fixes in addition to that.





### The deprecated `upload-script` feature was removed



The `upload-script` feature has been marked as deprecated for a very long time. In this release, it was completely removed, and it is no longer supported.




If you are using any of these capabilities:




* OpenID Connect Script Mapper
* Script Authenticator (Authentication Execution)
* JavaScript Policies




You should consider reading this [documentation](https://www.keycloak.org/docs/latest/server_development/#_script_providers) in order to understand how to still rely
on these capabilities but deploying your scripts to the server rather than managing them through the management interfaces.





### Session limits



Keycloak now supports limits on the number of sessions a user can have. Limits can be placed at the realm level or at the client level.




For more details, see [Server Administration Guide](https://www.keycloak.org/docs/25.0.6/server_admin/#_user_session_limits).
Thanks to [Mauro de Wit](https://github.com/mfdewit) for the contribution.





### SAML ECP Profile is disabled by default



To mitigate the risk of abusing SAML ECP Profile, Keycloak now blocks
this flow for all SAML clients that do not allow it explicitly. The profile
can be enabled using *Allow ECP Flow* flag within client configuration,
see [Server Administration Guide](https://www.keycloak.org/docs/25.0.6/server_admin/#_client-saml-configuration).





### Quarkus distribution



#### Import realms at startup



The Keycloak Quarkus distribution now supports importing your realms directly at start\-up. For more information, check the corresponding [guide](https://www.keycloak.org/server/importExport).





#### JSON and File Logging improvements



The Keycloak Quarkus distribution now initially supports logging to a File and logging structured data using JSON.




For more information on the improvements, check the corresponding [Logging](https://www.keycloak.org/server/logging) guide.




##### Environment variable expansion for values in keycloak.conf



The Keycloak Quarkus distribution now supports expanding values in keycloak.conf from environment variables.




For more information, check the corresponding [guide](https://www.keycloak.org/server/configuration).






#### New Option db\-url\-port



You can now change the port of your jdbc connection string explicitly by setting the new `db-url-port` configuration option. As for the other convenience options, this option will be overridden by the value of a full `db-url`, if set.





#### Split metrics\-enabled option into health\-enabled and metrics\-enabled



The `metrics-enabled` option now only enables the metrics for Keycloak. To enable the readiness and liveness probe, there’s the new build option `health-enabled`. This allows more fine\-grained usage of these options.






### Other improvements



* Account console alignments with latest PatternFly release.
* Support for encrypted User Info endpoint response. Thanks to [Giacomo Altiero](https://github.com/giacomoa)
* Support for the algorithm RSA\-OAEP with A256GCM used for encryption keys. Thanks to [Filipe Bojikian Rissi](https://github.com/fbrissi)
* Support for login with GitHub Enterprise server. Thanks to [Neon Ngo](https://github.com/nngo)







Keycloak 17\.0\.0
-----------------




### Highlights



#### Quarkus distribution is now fully supported



The default Keycloak distribution is now based on Quarkus. The new distribution is faster, leaner, and a lot easier to configure!




We appreciate migrating from the WildFly distribution is not going to be straightforward for everyone, since how you start and configure Keycloak has radically changed. With that in mind we will continue to support the WildFly distribution until June 2022\.




For information on how to migrate to the new distribution check out the [Quarkus Migration Guide](https://www.keycloak.org/migration/migrating-to-quarkus).





#### Quarkus distribution updates



A lot of effort went into polishing and improving the Quarkus distribution to make it as good as an experience as possible. A few highlights include:




* A new approach to documentation in form of server guides to help you install and configure Keycloak
* Upgraded Quarkus to 2\.7\.0\.Final
* Configuration file is no longer Java specific, and aligns configuration keys with CLI arguments
* Clearer separation between `build options` and `runtime configuration`.
* `h2-mem` and `h2-file` databases renamed to `dev-mem` and `dev-file`.
* Simplified enabling and disabling features
* Custom, and unsupported, Quarkus configuration is done through `conf/quarkus.properties`.
* Ability to add custom Java Options via JAVA\_OPTS\_APPEND (thanks to [dasniko](https://github.com/dasniko))
* Initial logging capabilities
* Initial support for Cross\-DC
* User\-defined profiles are no longer supported but using different configuration files to achieve the same goal
* Quickstarts updated to use the new distribution





#### Other improvements



##### Offline sessions lazily loaded



The offline sessions are now lazily fetched from the database by default instead of preloading during the server startup.





##### Improved User Search



Keycloak now supports a glob\-like syntax for the user search when listing users in the Admin Console,
which allows for three different types of searches: prefix (`foo*` which became the default search), infix (`*foo*`), and exact `"foo"`)









Keycloak 16\.1\.0
-----------------




### Highlights



#### Upgrade to Wildfly 26\.0\.0



Keycloak server was upgraded to use Wildfly 26\.0\.0\.Final as the underlying container.




For more information on WildFly 26 refer to the [WildFly 26 release notes](https://www.wildfly.org/news/2021/12/16/WildFly26-Final-Released/).








Keycloak 16\.0\.0
-----------------




### Highlights



#### Upgrade to Wildfly 25\.0\.1



Keycloak server was upgraded to use Wildfly 25\.0\.1\.Final as the underlying container.




WildFly 25 drops support for the legacy security subsystem, which is being replaced fully by Elytron. This requires significant changes to how Keycloak is configured. Please, refer to the migration guide for more details.




For more information on WildFly 25 refer to the [WildFly 25 release notes](https://www.wildfly.org/news/2021/10/05/WildFly25-Final-Released/).





#### Upgrade to Quarkus 2\.5\.3



Keycloak.X Quarkus preview distribution was upgraded to Quarkus 2\.5\.3\.








Keycloak 15\.1\.0
-----------------




### Highlights



#### Quarkus distribution preview



Without comparison the biggest highlight of this release is all the improvements that have been made to the Quarkus distribution. So many in fact, that it will be hard to list them all.




The CLI has been polished to hell and back, and we believe it now provides a very simple and convenient approach to configuring and running Keycloak. It’s almost so simple that documentation shouldn’t be needed.




To get started, just unpack the distribution, then type `bin/kc.[sh|bat] -h` to discover awesomeness!




That doesn’t mean we don’t plan to provide documentation for configuring Keycloak, but it didn’t quite make it this time around. In lack of documentation expect a blog post to follow the release introducing all the changes to the Quarkus distribution, as well as an overview on how to use it.




We are rapidly moving towards making the Quarkus distribution our default distribution, and will soon deprecate the WildFly distribution. With this in mind it is important that as many people as possible give it a test\-run and provide us with feedback if you find any usability issues, are not able to configure something with it, or if you discover any bugs.




We’d love to hear your thoughts and get your feedback in [GitHub Discussions](https://github.com/keycloak/keycloak/discussions/8654)!





#### New Admin Console preview



The new admin console is shaping up really nicely, and a preview is included in the main distribution. It is not quite feature complete yet, but there are still loads of things to try out.





#### WildFly update



Upgrading from WildFly 23 to WildFly 25 has taken a lot longer than we would have liked. We’re still working hard on this and are hoping to release Keycloak 16 as soon as possible with the upgrade, but as we wanted to get the updates to the Quarkus distribution out there we are doing this release in the meantime.





#### WildFly adapter deprecation



In WildFly 25 there is now excellent native OpenID Connect support without the need for the Keycloak adapter. With this in mind we are deprecating our WildFly adapter and will not support WildFly 25, but it will be around for a while for older WildFly versions and Red Hat JBoss Enterprise Application Platform 7\.y.





#### Spring Security and Boot adapter deprecation



A long time ago, with Spring Security 5\.0, there is now native support for OAuth 2\.0 and OpenID Connect in Spring. With this in mind now is the time to start deprecating our Spring Boot and Security adapters.





#### OpenID Connect Front\-Channel Logout Support



Keycloak now supports [OpenID Connect Front\-Channel Logout 1\.0](https://openid.net/specs/openid-connect-frontchannel-1_0.html).




For more details, take a look at [Server Administration Guide](https://www.keycloak.org/docs/25.0.6/server_admin/#_oidc-logout).




Thanks to [Ronaldo Yamada](https://github.com/rhyamada) for the contribution.





#### Deprecated features in the Keycloak Operator



With this release, we have deprecated and/or marked as unsupported some features in the Keycloak Operator. This
concerns the Backup CRD and the operator managed Postgres Database.








Keycloak 15\.0\.1
-----------------




### Highlights



This release contains some important bug fixes. In addition, We would like to thank [Leandro José de Bortoli](https://github.com/leandrobortoli) for his contributions to the
FAPI related functionalities such as JARM support and improvements in CIBA.







Keycloak 15\.0\.0
-----------------




### Highlights



#### Financial\-grade API (FAPI) Improvements, FAPI CIBA and Open Banking Brasil



The Keycloak server has improved support for the Financial\-grade API (FAPI). More specifically, Keycloak is now compliant with FAPI CIBA and with OpenBanking Brasil.
We also have support for CIBA ping mode. Thanks to [Takashi Norimatsu](https://github.com/tnorimat), who did most of the work on FAPI CIBA and who is
continually doing a really awesome job for the Keycloak project. Also thanks to [Dmytro Mishchuk](https://github.com/DmitryMishchuk),
[Andrii Murashkin](https://github.com/andriimurashkin), [Hryhorii Hevorkian](https://github.com/HryhoriiHevorkian) and [Leandro José de Bortoli](https://github.com/leandrobortoli), who did a great deal of
the work on the FAPI compliance as well. Finally thanks to all the members of the [FAPI Special interest group](https://github.com/keycloak/kc-sig-fapi/blob/main/members.adoc) for their help and feedback.








Keycloak 14\.0\.0
-----------------




### Highlights



#### Client Policies and Financial\-grade API (FAPI) Support



The Keycloak server has now official support for client policies and Financial\-grade API (FAPI). This capability was previewed in earlier versions, but now
it is more polished and properly documented. Thanks to [Takashi Norimatsu](https://github.com/tnorimat), who did most of the work on this. Also thanks
to [Dmytro Mishchuk](https://github.com/DmitryMishchuk), [Andrii Murashkin](https://github.com/andriimurashkin) and [Hryhorii Hevorkian](https://github.com/HryhoriiHevorkian), who did a great deal of the work on this feature as well.
Finally thanks to all the members of the [FAPI Special interest group](https://github.com/keycloak/kc-sig-fapi/blob/main/members.adoc) for their help and feedback.





#### Improvements to User Profile SPI and support for declarative configuration



In this version, there were several improvements to the User Profile SPI in order
to prepare the ground on how users profiles are managed in Keycloak.




One of these improvements is the support for configuring user profiles through the administration console. For more
details proceed to [Server Administration Guide](https://www.keycloak.org/docs/25.0.6/server_admin/#user-profile)




Thanks to the community and all the individuals involved in this effort.





#### Improvements to offline sessions



Offline session preloading has been improved and should be faster thanks to [Peter Flintholm](https://github.com/Flintholm).




As a preview feature, offline session preloading can be skipped in favor of lazy loading thanks
to [Thomas Darimont](https://github.com/thomasdarimont)'s efforts. This feature has to be explicitly
activated in the server configuration, see Server administration guide for details.





#### Other improvements



* The support for configuring maximum number of active authentication sessions. The default value is set to 300 authentication sessions (browser tabs) per a browser’s session








Keycloak 13\.0\.0
-----------------




### Highlights



#### Upgrade to Wildfly 23



The Keycloak server was upgraded to use Wildfly 23\.0\.2\.Final as the underlying container.





#### OAuth 2\.0 Device Authorization Grant (RFC 8628\)



Support for OAuth 2\.0 Device Authorization Grant is now available.




Thanks to
Hiroyuki Wada, [Łukasz Dywicki](https://github.com/splatch)
and [Michito Okai](https://github.com/Michito-Okai).





#### OpenID Connect Client Initiated Backchannel Authentication (CIBA)



Support for OpenID Connect Client Initiated Backchannel Authentication (CIBA) is now available.




Thanks to [Takashi Norimatsu](https://github.com/tnorimat),
[Andrii Murashkin](https://github.com/andriimurashkin), [Christophe Lannoy](https://github.com/c4r1570p4e) and members of the FAPI WG for the implementation and feedback.





#### SAML Artifact binding in server to client communication



Keycloak now supports communication with clients using SAML *Artifact* binding. A new `Force Artifact Binding` option
was introduced in the client configuration, that forces communication with the client using artifact messages. For more
details proceed to [Server Administration Guide](https://www.keycloak.org/docs/25.0.6/server_admin/#_client-saml-configuration). Please note, that with
this version, Keycloak SAML client adapter does NOT support Artifact binding.




Thanks to [AlistairDoswald](https://github.com/AlistairDoswald) and [harture](https://github.com/harture).





#### Support PKCE for identity brokering



Keycloak can now leverage PKCE when brokering to an external OpenID Connect IdP.




Thanks to [thomasdarimont](https://github.com/thomasdarimont).





#### Default roles processing improvement



Default roles are now internally stored as composite roles of a new role usually named `default-roles-<realmName>`. Instead of assigning
both realm and all client default roles directly to newly created users or users imported through Identity Brokering, just the role is
assigned to them and the rest of default roles are assigned as effective roles. This change improves performance of default roles processing,
especially with larger number of clients, because it is no longer necessary to go through all clients.








Keycloak 12\.0\.0
-----------------




### Highlights



#### Keycloak.X distribution preview



Introduction a preview of the new and upcoming Keycloak.X distribution. This distribution is powered by Quarkus, bringing
significant improvements to startup time and memory consumption, as well as making it a lot easier to configure Keycloak.





#### New Account console is now the default



The new account console is no longer a preview feature and is now the default account console in Keycloak. The old account
console will stay around for a while. For those that have a custom theme for the old account console the old console
will be used by default, giving you the time to update your custom theme to the new account console.





#### OpenID Connect Back\-Channel Logout



Support for OpenID Connect Back\-Channel Logout is now available, thanks to [DaSmoo](https://github.com/DaSmoo) and
[benjamin37](https://github.com/benjamin37).





#### Upgrade to Wildfly 21



The Keycloak server was upgraded to use Wildfly 21 as the underlying container.





#### Ability to request AuthnContext in SAML identity provider



Support for specification of AuthnContext section in authentication requests issued by SAML identity provider has been added.




Thanks to [lscorcia](https://github.com/lscorcia)





#### FAPI RW support and initial support to Client policies



There was lots of the work done to have support for Financial\-grade API Read and Write API Security Profile (FAPI RW). This is available
with the usage of Client policies and it is still in the preview state. You can expect more polishing in the next releases.
Thanks to [Takashi Norimatsu](https://github.com/tnorimat) and all the members of the [FAPI Special interest group](https://github.com/keycloak/kc-sig-fapi).





#### Upgrade login theme to PatternFly 4



The Keycloak login theme components have been upgraded to PatternFly 4\.
The old PatternFly 3 runs simultaneously with the new one, so it’s possible to have PF3 components there.




There are also design changes in the login theme for better user experience.
You can even define an icon for your custom Identity providers.
For details, please refer to the [docs](https://www.keycloak.org/docs/25.0.6/server_development/#custom-identity-providers-icons).





#### Gatekeeper EOL



Gatekeeper reached end of life, in November 21\. This means that we no longer support, or update it. The announcement is available [here](https://www.keycloak.org/2020/08/sunsetting-louketo-project.adoc).





#### Other improvements



* Support for OAuth2 Client Credentials grant without refresh token and without user session. Thanks to [Thomas Darimont](https://github.com/thomasdarimont)
* Support for send access tokens to the OAuth2 Revocation endpoint








Keycloak 11\.0\.0
-----------------




### Highlights



#### LDAPv3 password modify operation



Support for LDAPv3 password modify operation was added. Also the ability in the admin console to request metadata from the configured
LDAP server to see if it supports LDAPv3 password modify operation.




Thanks to [cachescrubber](https://github.com/cachescrubber)





#### Namespace support for LDAP group mapper



Namespace support for LDAP group mapper allows you to map groups from LDAP under specified branch (namespace) of the Keycloak groups tree.
Previously groups from LDAP were always added as the top level groups in Keycloak.




Thanks to [Torsten Juergeleit](https://github.com/tjuerge)





#### Upgrade to WildFly 20



Keycloak server was upgraded to use WildFly 20\.0\.1\.Final under the covers. For more details,
please take a look at [Upgrading Guide](https://www.keycloak.org/docs/latest/upgrading/).





#### SAML POST binding is broken in the latest versions of browsers



The `SameSite` value `None` for `JSESSIONID` cookie is necessary for correct behavior of the Keycloak SAML adapter.
Usage of a different value is causing resetting of the container’s session with each request to Keycloak, when
the SAML POST binging is used. Refer to the following steps for
[Wildfly](https://www.keycloak.org/docs/25.0.6/securing_apps/#_saml-jboss-adapter-samesite-setting) to keep the correct behavior. Notice, that this
workaround should be working also with the previous versions of the adapter.





#### Other improvements



* Support for client offline session lifespan. Thanks to [Yoshiyuki Tabata](https://github.com/y-tabata)
* Czech translation. Thanks to [Jakub Knejzlík](https://github.com/jakubknejzlik)
* Possibility to fetch additional fields from the Facebook identity provider. Thanks to [Bartosz Siemieńczuk](https://github.com/BartoszSiemienczuk)
* Support for AES 192 and AES 256 algorithms used for signed and encrypted ID tokens. Thanks to [Takashi Norimatsu](https://github.com/tnorimat)
* Ability to specify signature algorithm in Signed JWT Client Authentication. Thanks to [Takashi Norimatsu](https://github.com/tnorimat)








Keycloak 10\.0\.0
-----------------




### Highlights



#### Identity Brokering Sync Mode



With Identity Brokering Sync Mode it is now possible to control if user profiles are updated on first login, or
every login from an external Identity Provider. It is also possible to override this behaviour on individual mappers.




Thanks to [Martin Idel](https://github.com/Martin-Idel-SI)





#### Client Session Timeout for OpenID Connect / OAuth 2\.0



Typically, an SSO session last for days if not months, while individual client sessions should ideally be a lot shorter.
With the introduction of client session timeout it is now possible to configure a separate timeout for individual clients,
as well as a default for all clients within a realm.




Thanks to [Yoshiyuki Tabata](https://github.com/y-tabata)





#### OAuth 2\.0 Token Revocation (RFC 7009\)



For applications that use Keycloak as an OAuth 2\.0 Authorization Server there is now support to revoke refresh tokens
through the token revocation endpoint.




Thanks to [Yoshiyuki Tabata](https://github.com/y-tabata)





#### Security Headers SPI and Response Filter



A new SPI was introduced to allow better flexibility when setting security related headers on responses. This provides
a cleaner implementation within Keycloak, but also allows full customisation if needed. Security headers are now set
by a response filter instead of within the code itself, which makes it less error\-prone, removing the chance that
some response are missing headers.





#### Upgrade to WildFly 19



Keycloak server was upgraded to use WildFly 19 under the covers.





#### Other improvements



* Support for invoking Application Initiated Actions added to Keycloak JavaScript adapter
* Performance improvements to fetching resources and policies during evaluation








Keycloak 9\.0\.1
----------------




### Highlights



#### PromiseType removed from JavaScript adapter



The promiseType init option has been removed from the JavaScript adapter. Instead a promise that supports
both native promise API and legacy Keycloak promise API is returned. This allows gradually migration of
applications from the legacy/deprecated API to the native promise API.






### Other improvements



#### Reverted breaking API changes to LocaleSelectorSPI



In 9\.0\.0 a breaking API change was introduced to LocaleSelectorSPI. With 9\.0\.1 the changes to
this API is now reverted, and a new LocaleUpdaterSPI has been introduced.





#### Fixed the automatic resolution of `KeycloakConfigResolver` instances for Spring Boot Applications



In previous releases, Spring Boot applications had to manually implement the `KeycloakConfigResolver` interface or extend the
built\-in `org.keycloak.adapters.springboot.KeycloakSpringBootConfigResolver`.




This release fixes the backward compatibility issue by resolving instances automatically in case none is provided. As well as still
allowing applications to provide their own configuration resolver implementations.








Keycloak 9\.0\.0
----------------




### Highlights



#### Drools Policy Removed



The Drools Policy was finally removed after the deprecation period. If you need more complex policies you can still use JavaScript\-based policies.





#### Pagination support for clients



Pagination support was added to clients in the Admin Console and REST API. Thanks to [saibot94](https://github.com/saibot94).





#### New Elytron Credential Store Vault Provider



A new built\-in vault provider that reads secrets from a keystore\-backed Elytron credential store has been added as a WildFly
extension. The creation and management of the credential store is handled by Elytron using either the `elytron` subsystem or the
`elytron-tool.sh` script.





#### More updates to W3C WebAuthn and Authentication flows



In this release, we did some usability improvements to the authentication flows. It should be easier for the end user to choose between
available authentication mechanisms for two\-factor authentication. It should be more intuitive to log in with OTP or WebAuthn
considering the fact that user can have more OTP or WebAuthn credentials. There is also better support for passwordless WebAuthn authentication.
Finally, we did some work on defects related to the authentication flows.





#### Improved handling of user locale



A number of improvements have been made to how the locale for the login page is selected, as well as when the locale
is updated for a user.





#### Other improvements



* Authorization Header token is only considered now when type is Bearer on Gatekeeper. Thanks to [HansK\-p](https://github.com/HansK-p)
* More algorithms are supported for the client authentication with signed client secret JWT. Namely HS384 and HS512 algorithms were added.
Thanks to [tnorimat](https://github.com/tnorimat)








Keycloak 8\.0\.2
----------------




### Highlights



#### SameSite cookie changes with upcoming Google Chrome update



Starting with version 80, Google Chrome will change the default value for the `SameSite` cookie parameter to `Lax`.
Therefore, changes were required to several Keycloak cookies (especially those which are used within the
Javascript adapter for checking the session status using the iframe) to set `SameSite` parameter to `None`. Please note
that this setting also requires setting the `Secure` parameter, hence starting with this version, the Javascript
adapter will only be fully functional when using the SSL / TLS connection on the Keycloak side.








Keycloak 8\.0\.1
----------------




### Highlights



#### LDAP Issue



This release fixes a critical vulnerability in LDAP introduced in Keycloak 7\. If you are using Keycloak 7\.0\.0, 7\.0\.1 or
8\.0\.0 in production we strongly suggest that you upgrade immediately.





#### WildFly 18\.0\.1\.Final



Upgrade to WildFly 18\.0\.1\.Final which includes updates to a number of CVEs in third\-party libraries.








Keycloak 8\.0\.0
----------------




### Highlights



#### Vault



Several configuration fields can obtain their value from
a vault instead of entering the value directly: LDAP bind password,
SMTP password, and identity provider secrets.




Furthermore, new vault SPI has been introduced to enable development
of extensions to access secrets from custom vaults.





#### New Default Hostname provider



The fixed and request hostname providers have been replaced with a single new default hostname provider. This provider
comes with a number of improvements, including:




* No need to change provider to set fixed base URL
* Support different base URL for frontend and backend requests
* Support changing context\-path in cases where Keycloak is exposed on a different context\-path through a reverse proxy





#### Messages in theme resources



Message bundles in theme resources enables internationalization of custom providers such as authenticators. They are also shared between all theme types, making it possible to for example share messages between the login and account console. Thanks to [micedre](https://github.com/micedre).





#### RoleMappingsProvider SPI for the SAML adapters



We have added a new SPI that allows for the configuration of custom role mappers that are used by the SAML adapters to map
the roles extracted from the SAML assertion into roles that exist in the SP application environment. This is particularly useful
when the adapters need to communicate with third party IDPs and the roles set by the IDP in the assertion do not correspond to
the roles that were defined for the SP application. The provider to be used can be configured in the `keycloak-saml.xml`
file or in the `keycloak-saml` subsystem. An implementation that performs the role mappings based on the contents of a properties
file was also provided.




Notice that when Keycloak acts as the IDP we can use the built\-in role mappers to perform any necessary mappings
before setting the roles into the assertion, so this SPI will probably be redundant in this case. The `RoleMappingsProvider`
SPI was designed for situations when the IDP offer no way to map roles before adding them to the assertion.





#### WildFly 18 Upgrade



Keycloak server was upgraded to use WildFly 18 under the covers.





#### W3C Web Authentication support



In this release, we added initial support for W3C Web Authentication (WebAuthn). There are a few limitations in current implementation,
however we are working on further improvements in this area. Thanks to [tnorimat](https://github.com/tnorimat) for the contribution. Also thanks to
ynojima for the help and feedback.





#### Support for password\-less authentication, multi\-factor authentication and multiple credentials per user



With the arrival of W3C Web Authentication support, we’ve refined the authentication flow system to be able to allow a user to select which authentication method is preferred for login (for example, the choice between an OTP credential and a WebAuthn credential). The new mechanisms also allow an administrator to
craft flows for password\-less login, for example just using WebAuthn as an authentication method. Please note that with these changes, any custom authentication
flow you have created may need to be adapted to the new flow logic.




As a result of these changes, users can now have multiple OTP devices and multiple WebAuthn devices. The same system that allows a user
to select which type of device to use during login also allows that user to select which specific device to use. Thanks to the [Cloudtrust](https://github.com/cloudtrust) team:
[AlistairDoswald](https://github.com/AlistairDoswald), [sispeo](https://github.com/fperot74) and [Fratt](https://github.com/Fratt) for their contributions, and
to [harture](https://github.com/harture) and [Laurent](https://github.com/lagess) for their help.






### Other Improvements



#### System properties and environment variables support in theme.properties



It is now possible to use system properties and environment variables within theme.properties file. Thanks to [Opa\-](https://github.com/Opa-)





#### Support more signing algorithms for client authentication with signed JWT



Thanks to [tnorimat](https://github.com/tnorimat), we support more signing algorithms for client authentication with signed JWT.





#### Configurable client authentication method for OIDC Identity providers



In this release, possibility to authenticate OIDC providers with signed JWT or basic authentication was added. So all the client
authentication methods mentioned in the [OIDC specification](https://openid.net/specs/openid-connect-core-1_0.html#ClientAuthentication)
are supported now. Thanks to [madgaet](https://github.com/madgaet) and [rradillen](https://github.com/rradillen) for contributions.





#### Support enable/disable logging into the JavaScript adapter



Thanks to [jonkoops](https://github.com/jonkoops) now it’s possible to enable or disable logging for the JS adapter.





#### Credentials support removed from the JavaScript adapter



The option to provide client credentials in the JavaScript adapter was removed. Thanks to [jonkoops](https://github.com/jonkoops)





#### Updates for Gatekeeper



* Secure token and logout endpoint were included in Gatekeeper. Thanks to [fredbi](https://github.com/fredbi)
* There was a bug on Gatekeeper which was making cookies to be applied to subdomains. Thanks to [daniel\-ac\-martin](https://github.com/daniel-ac-martin) the issue was fixed
* Now Gatekeeper provides support to Same\-site cookies. Thanks to [fiji\-flo](https://github.com/fiji-flo)





#### Deploying Scripts to the Server



Please take a look at [7\.0\.1 Release Notes](https://www.keycloak.org/docs/25.0.6/release_notes/#keycloak-7-0-1) for more details on how you can now deploy and run scripts to customize specific behavior.








Keycloak 7\.0\.1
----------------




### Deploying Scripts to the Server



Until now, administrators were allowed to upload scripts to the server through the Keycloak Administration Console as well as
through the RESTful Admin API.




For now on, this capability is **disabled** by default and users should prefer to deploy scripts directly to the server. For more details,
please take a look at [JavaScript Providers](https://www.keycloak.org/docs/25.0.6/server_development/#_script_providers).







Keycloak 7\.0\.0
----------------




### Highlights



#### WildFly 17 Upgrade



Keycloak server was upgraded to use WildFly 17 under the covers.





#### Tomcat 9 adapter support



Java adapter for Apache Tomcat 8 and Apache Tomcat 9 was unified and now it serves for both of them.





#### New Account Console



A lot of work has been done on the new Account Console and Account REST API. It’s not quite ready yet, but it’s getting
there and hopefully will be fully done for Keycloak 8\.





#### Signed and Encrypted ID Token Support



Keycloak can support the signed and encrypted ID token according to the Json Web Encryption (JWE) specification. Thanks to [tnorimat](https://github.com/tnorimat).





#### Testing and release automation



The Keycloak team has spent a significant amount of time on automation around testing and releases both for Keycloak and
Red Hat Single Sign\-On.






### Other improvements



* PKCE support added to JavaScript adapter. Thanks to [thomasdarimont](https://github.com/thomasdarimont)
* Oracle database support added to Keycloak container image. Thanks to [nerdstep](https://github.com/nerdstep)
* Clock Skew support added to SAML adapter. Thanks to [steevebtib](https://github.com/steevebtib)
* TypeScript support for Node.js adapter. Thanks to [evanshortiss](https://github.com/evanshortiss)
* Gatekeeper now allows to provide unencrypted token in header, while encrypting in cookie. There was also a bug on Gatekeeper when `Revoke Refresh Token` is enabled on the Keycloak server. The issue was fixed. Thanks to [fredbi](https://github.com/fredbi)
* New tab in the Admin console to display the list of users for client roles. Thanks to [unly](https://github.com/unly)







Keycloak 6\.0\.0
----------------




### WildFly 16 Upgrade



Keycloak server was upgraded to use WildFly 16 under the covers.




#### SmallRye Health and Metrics extensions



Keycloak now comes enabled with the SmallRye Health and Metrics extensions which provides standard health and metrics
endpoints. We will add some documentation as well as Keycloak specific metrics soon.






### PS256 support



Thanks to [tnorimat](https://github.com/tnorimat) Keycloak now has support for signing and verifying tokens with PS256\.





### MP\-JWT Client Scope



New built\-in client scope to make it easy to issue tokens following the Eclipse MicroProfile specification.







Keycloak 5\.0\.0
----------------




### WildFly 15 Upgrade



Keycloak server was upgraded to use WildFly 15 under the covers.







Keycloak 4\.8\.0\.Final
-----------------------




### OpenShift Integration



It is now possible to fully secure OpenShift 3\.11 with Keycloak, including the ability to automatically expose
Service Accounts as OAuth clients as clients to Keycloak.




This is currently a technology preview feature.





### Rules/Drools Policy Marked as a Technology Preview Feature



Until now, Drools policies were enabled by default. But now, this policy type is only available as a technology preview feature and
to use it you need to enable the preview profile or the corresponding feature. Take a look at the [Authorization Services Guide](https://www.keycloak.org/docs/25.0.6/authorization_services/) for more details.





### Support for DB2 removed



DB2 support has been deprecated for a while. With this release we have removed all support for DB2\.







Keycloak 4\.7\.0\.Final
-----------------------




### Enhanced Remember Me



Introduced the ability to specify different session idle and max timeouts for remember me sessions. This enables remember
me sessions to live longer than regular sessions.





### Pagination support for Groups



Large numbers of groups have previously caused issues in the admin console. This is now resolved by the introduction of
pagination of groups.





### Improve startup time with large number of offline sessions



In the past, starting the server could take a long time if there were many offline sessions. This startup time has now
been significantly reduced.







Keycloak 4\.6\.0\.Final
-----------------------




### Upgrade to WildFly 14



The Keycloak server was upgraded to use WildFly 14 under the covers.





### Keycloak Gatekeeper



Keycloak Gatekeeper provides a security proxy that can be used to secure applications and services without an adapter.
It can be installed locally alongside your application or as a sidecar on OpenShift or Kubernetes.




Huge thanks to [gambol99](https://github.com/gambol99) for contributing this work to Keycloak.







Keycloak 4\.5\.0\.Final
-----------------------




### Signature SPI



The Signature SPI makes it possible to plug\-in additional signature algorithms. This enables additional signatures and also enables changing how signatures are generated. For example, using this allows using an HSM device to sign tokens.




Thanks to [tnorimat](https://github.com/tnorimat) for contributing a significant part of this work.





### New Signature Algorithms



Alongside the Signature SPI there is now also support for additional signature algorithms.




Keycloak now has support for RS256, RS384, RS512, ES256, ES384, ES512, HS256, HS384 and HS512\.




Elliptic Curve Digital Signature Algorithm (ES256/384/512\) are very interesting as they provide similar
security properties as RSA signatures, but use significantly less CPU.




HMAC (HS256/384/512\) are also very useful when you do not want your application to verify the signature itself.
Since these are symmetric signatures only Keycloak is able to verify the signature, which requires the
application to use the token introspection endpoint to verify tokens.




Thanks to [tnorimat](https://github.com/tnorimat) for contributing a significant part of this work.





### Better Audience Support for OpenID Connect clients



It is now possible to specify the audiences in the tokens issued for OpenID Connect clients. There is also support for verification
of audience on the adapter side.





### Minor improvements



* Added LocaleSelector SPI, which allows to change the way how the locale will be resolved for a particular request. Thanks to [knutz3n](https://github.com/knutz3n)
* Added an authenticator to automatically link Identity Provider identity to an existing account after first Idp authentication. Thanks to [slominskir](https://github.com/slominskir)







Keycloak 4\.4\.0\.Final
-----------------------




### Upgrade to WildFly 13



The Keycloak server was upgraded to use WildFly 13 under the covers. This means update of the underlying dependencies and also
some changes in the configuration. We now also support WildFly 13 adapter and we upgraded the underlying JDG/Infinispan server version for
the Cross\-DC setup. See [Upgrading Guide](https://www.keycloak.org/docs/25.0.6/upgrading/) for more details.





### Authorization Services support in Node.js



Having authorization services support in Node.js makes it very easy to do fine\-grained central authorization
with the Node.js adapter.





### Minor improvements



* Update design for the welcome page
* Allow passing current locale to OAuth2 IdPs. Thanks to [knutz3n](https://github.com/knutz3n)
* Support Content\-Security\-Policy\-Report\-Only security header. Thanks to [knutz3n](https://github.com/knutz3n)
* Script based ProtocolMapper for SAML. Thanks to [AlistairDoswald](https://github.com/AlistairDoswald)







Keycloak 4\.3\.0\.Final
-----------------------




### Hostname SPI



The hostname SPI introduces a more flexible way to configure the hostname for Keycloak. There are two
built\-in providers. The first is request, which uses the request headers to determine the hostname. The second
is fixed, which allows configuring a fixed hostname. The latter makes sure that only valid hostnames can be
used and also allows internal applications to invoke Keycloak through an alternative URL.




For more details refer to the threat mitigation section in the [Server Administration Guide](https://www.keycloak.org/docs/25.0.6/server_admin/).





### X509 Client Authenticator



The newly added Client Authenticator uses X509 Client Certificates and Mutual TLS to secure a connection from the client. In addition to that
the Keycloak Server validates Subject DN field of the client’s certificate.





### Performance improvements to Authorization Services



For this release, we improved policy evaluation performance across the board, increasing reliability and throughput. The main
changes we did were related with trying to optimize the policy evaluation path by avoiding unnecessary flows and collect decisions
as soon as they happen. We also introduced a policy decision cache on a per\-request basis, avoiding redundant decisions from policies
previously evaluated.




We are also working on other layers of cache which should give a much better experience. See [KEYCLOAK\-7952](https://issues.redhat.com/browse/KEYCLOAK-7952).





### Choosing the response mode when obtaining permissions from the server



In previous versions, permissions were always returned from the server using standard OAuth2 response, containing the access and refresh tokens. In this release,
clients can use a `response_mode` parameter to specify how the server should respond to an authorization request. This parameter accepts two values:




* `decision`



Indicating that responses should only contain a flag indicating whether or not permissions were granted by the server. Otherwise a `403` HTTP status code is returned.
* `permissions`



Indicating that a response should contain every single permission granted by the server using a JSON format.





### NodeJS Policy Enforcer



The [keycloak\-nodejs\-connect](https://github.com/keycloak/keycloak-nodejs-connect), an adapter for NodeJS, now supports constructs to protect
resources based on decisions taken from the server. The new construct allows users to protect their resources using fine\-grained permissions as follows:






```
app.get('/protected/resource', keycloak.enforcer('resource:view'), function (req, res) {
  res.json({message: 'access granted'});
});
```





### Support hosted domain for Google logins



Login with Google now supports the `hd` parameter to restrict Google logins to a specific hosted domain at Google. When
this is specified in the identity provider any login from a different domain is rejected.




Thanks to [brushmate](https://github.com/brushmate) for the contribution.





### Escape unsafe tags in HTML output



Most HTML output is already escaped for HTML tags, but there are some places where HTML tags are permitted.
These are only where admin access is needed to update the value. Even though it would require admin access to update such
fields we have added an extra layer of defence and are now escaping unsafe elements like `<script>`.







Keycloak 4\.2\.0\.Final
-----------------------




### Browser tab support for Cordova



We now have support for using browser tab and universal links in the JavaScript adapter for Cordova. This enables SSO
between multiple applications as well as increases security.




Thanks to [gtudan](https://github.com/gtudan) for the contribution.





### SAML adapter multitenancy support



The SAML adapter can support multi\-tenancy now just like the built\-in adapter for OpenID Connect.





### An option to create claims with dots (.) in them



In previous versions, it was not possible to create claims in the token using a claim name containing a dot (.) character. Now it is
possible to escape the dot character in the configuration, so a claim name with the dot character can be used.







Keycloak 4\.1\.0\.Final
-----------------------




### Making Spring Boot 2 the default starter



Starting with release 4\.1, the Spring Boot starter will be based on the Spring Boot 2 adapter. If you are using an older Spring Boot version, the keycloak\-legacy\-spring\-boot\-starter is available.







Keycloak 4\.0\.0\.Final
-----------------------




### Client Scopes and support for OAuth 2 scope parameter



We added support for Client Scopes, which replaces Client Templates. Client Scopes are a more flexible approach and also provides
better support for the OAuth `scope` parameter.




There are changes related to Client Scopes to the consent screen. The list on the consent screen is now linked to client scopes
instead of protocol mappers and roles.




See the documentation and migration guide for more details.





### OAuth 2 Certificate Bound Access Tokens



We now have a partial implementation of the specification
[OAuth 2\.0 Mutual TLS Client Authentication and Certificate Bound Access Tokens](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-mtls-08) .
More accurately we have support for the Certificate Bound Access Tokens. If your confidential client is able to use 2\-way SSL,
Keycloak will be able to add the hash of the client certificate into the tokens issued for the client. At this moment,
it’s just the Keycloak itself, which verifies the token hashes (for example during `refresh token` requests).
We plan to add support to adapters as well. We also plan to add support for Mutual TLS Client Authentication.




Thanks to [tnorimat](https://github.com/tnorimat) for the contribution.





### Authorization Services



#### UMA 2\.0 Support



UMA 2\.0 is now supported for Authorization Services. Check the documentation for more details
if you are coming from previous versions of Keycloak.




##### User\-Managed Access through the Keycloak Account Service



Now end\-users are able to manage their resources and the permissions associated with them through the Keycloak Account Service.
From there, resource owners can now check their resources, share resources with another users as well approve requests from other users.





##### Asynchronous Authorization Flow



When using UMA, client applications can now choose whether or not an authorization request should start an authorization flow
to ask for the resource owner approval. This functionality allows applications to ask for resource owner
approval when trying to access one of his resources on behalf of another user.





##### User\-Managed Permission API



Resource servers are now capable of associating additional policies to resources owned by a particular user. The new API provides
operations to manage these permissions using different policy types such as role, group, user, client or a condition using JavaScript.






#### Pushed Claims



Clients applications are now able to send arbitrary claims to Keycloak along with an authorization request in order to
evaluate permissions based on these claims. This is a very handy addition when access
should be granted (or denied) in the scope of a specific transaction or based on information about the runtime.





#### Resource Attributes



It is now possible to associated attributes with resources protected by Keycloak and use these same attributes to evaluate permissions
from your policies.





#### Policy enforcer now accepts regular access tokens



In some situations, you may want to just send regular access tokens to a resource server but still be able to enforce policies on these resources.




One of the main changes introduced by this release is that you are no longer required to exchange access tokens with RPTs in
order to access resources protected by a resource server (when not using UMA). Depending on how the policy enforcer is configured on the resource server side, you can just send regular
access tokens as a bearer token and permissions will still be enforced.





#### Policy enforcer can now load resources from the server on\-demand



Until now, when deploying an application configured with a `policy-enforcer`, the policy enforcer would either load all protected paths
from the server or just map these paths from the adapter configuration. Users can now decide to load paths on\-demand from the server and avoid
map these resources in the adapter configuration. Depending on how many protected resources you have this functionality can also improve the time to
deploy an application.





#### Policy enforcer now supports configuring the resource cache



In order to avoid unnecessary hits to the server, the policy enforcer caches the mapping between protected resources and their corresponding paths
in your application. Users can now configure the behaviour of the cache or even completely disable it.





#### Claim Information Points



The `policy-enforcer` definition on the adapters (`keycloak.json`) was also updated to support the concept of pushed claims. There
you have the concept of a `claim-information-point` which can be set to push claims from different sources such as the HTTP request or even
from an external HTTP service.





#### Improvements to the Evaluation API



The Evaluation API used to implement policies in Keycloak, especially JavaScript and Drools policies, provides now methods to:




* Access information from the current realm such as check for user roles, groups and attributes
* Push back arbitrary claims to the resource server in order to provide additional information on how a specific permissions should
be enforced






### Authorization Services



#### UMA 2\.0



UMA 2\.0 is now supported for Authorization Services, including support for users to manage user access through
the account management console. There are also other additions and improvements to authorization services.





#### Pushed Claims



Clients can now push additional claims and have them used by policies when evaluating permissions.





#### Resource Attributes



It is now possible to define attributes on resources in order to have them used by policies when evaluating permissions.






### Themes and Theme Resources



It is now possible to hot\-deploy themes to Keycloak through a regular provider deployment. We have also added support for theme resources, which allows adding additional templates and resources without creating a theme. This is useful for custom authenticators that require additional pages to be added to the authentication flow.




We have also added support to override the theme for specific clients. If that is not adequate for your needs, then there is also a new Theme Selector SPI that allows you to implement custom logic to select the theme.





### Instagram Identity Provider



We have added support to login with Instagram. Thanks to [hguerrero](https://github.com/hguerrero) for the contribution.





### Search by User ID in Admin Console



To search for a user by id in the admin console you previously had to edit the URL. It is now possible to search
directly in the user search field.





### Adapters



#### Spring Boot 2



We now have support for Spring Boot 2\.





#### Fuse 7



We now have support for Fuse 7\.





#### JavaScript \- Native Promise Support



The JavaScript adapter now supports native promises. It retains support for the old style promises as well.
Both can be used interchangeably.





#### JavaScript \- Cordova Options



It is now possible to pass Cordova\-specific options to login and other methods in the JavaScript adapter.
Thanks to [loorent](https://github.com/looorent) for the contribution.










Last updated 2024\-09\-19 17:43:02 UTC





