import google.generativeai as genai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
# Configure the API key for Google Generative AI
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Initialize the generative model
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
)

# Generate a travel itinerary using the model
def generate_itinerary(source, destination, start_date, end_date, instructions):
    response = model.generate_content(
        f"Create a detailed travel itinerary for a trip from {source} to {destination} from {start_date} to {end_date}, including places to visit, activities for each day, and an estimated budget. Highlight weather conditions with on that day, and clothes to wear accordingly. Also, include the following additional instructions: {instructions}. Present the budget in a table with strict borders, showing costs for Flights, Accommodation, Food, Transportation, Sightseeing. Ensure clear separation between sections (itinerary, table) and strict spacing between table rows and columns. Provide a total estimated budget at the end."
    )
    print(response.text)  # Print the response text from the AI model
    return (response.text)  # Return the generated itinerary
