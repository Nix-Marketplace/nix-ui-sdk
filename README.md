# nix-ui-sdk
A light customisation of NiceGUI for building webapps on Nix. The goal is to make turning a script -> web app/product as easy as possible for developers, without having to think about auxiliary/business stuff (e.g., auth, getting API keys, design). All developers need to focus on is making an awesome function or tool that could work in a CLI - we handle the rest.

Changes to the main NiceGUI library fall broadly under one of three categories:
1. **Opinionated UI elements**; we set sensible default settings for NiceGUI elements that align with the rest of the site (e.g., colour, size, validations, font) so that developers don't have to think about tools looking nice.
2. **New UI elements**; NiceGUI extends Quasar so we can basically create any components that commonly pop up for developers or combine existing NiceGUI elements in interesting ways, reducing the amount of frontend work required (e.g., creating a 'basic auth' component that automatically sets up a username and password input field in a row)
3. **Analytics & integration with platform**; hooks in the NiceGUI app lifecycle to enable usage tracking of resources (e.g., compute, API calls), as well as passing useful data to builders (e.g., OAuth2 tokens and API keys for services)
