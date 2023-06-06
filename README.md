# EnergyUsage

---- This is all for the free sandbox API!! NOT FOR LIVE ENV  -------- 


• Error Handling: Implemented error handling to handle potential exceptions that may occur during the API request such as invalid API key, network errors, or unexpected responses.

• Pagination: Although pagination is not fully implemented in the Voltus API sandbox, I simulated pagination by modifying the code to handle paginated responses. Updated the code to request subsequent pages if available and merge the results into a single list of sites.

• Interactive User Interface: Developed a command-line interface (CLI) to interact with the project. Allows users to input their API key, view the list of sites, and navigate through paginated results if applicable.

• Additional Site Details: Expand the information displayed for each site. Retrieves and displays additional details such as the site's customer location ID, meters associated with the site (including their names and IDs), and any other relevant information provided by the API response.

• Filtering and Sorting: Implemented filters and sorting options to refine the displayed sites. Allows users to filter sites based on certain criteria (e.g., site name, customer location ID) and sort the sites based on different attributes (e.g., alphabetical order, number of meters).

• Caching and Refreshing: Implemented a caching mechanism to store the retrieved site data locally. Allows users to refresh the data from the API or retrieve it from the cache to minimize API calls and improve performance.
