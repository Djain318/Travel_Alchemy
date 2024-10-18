# Travel Alchemy - Your Personalized Travel Planner

<div align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.8%2B-blue.svg" alt="Python" style="margin: 5px;"></a>
  <a href="https://flask.palletsprojects.com/"><img src="https://img.shields.io/badge/Flask-2.0.2-green.svg" alt="Flask" style="margin: 5px;"></a>
  <a href="https://getbootstrap.com/"><img src="https://img.shields.io/badge/Bootstrap-4.5.2-lightblue.svg" alt="Bootstrap" style="margin: 5px;"></a>
  <a href="https://daringfireball.net/projects/markdown/"><img src="https://img.shields.io/badge/Markdown-v1.0.0-orange.svg" alt="Markdown"></a>

<a href="https://developer.mozilla.org/en-US/docs/Web/HTML"><img src="https://img.shields.io/badge/HTML-5-orange.svg" alt="HTML"></a>
<a href="https://developer.mozilla.org/en-US/docs/Web/CSS"><img src="https://img.shields.io/badge/CSS-3-purple.svg" alt="CSS" style="margin: 5px;"></a>
<a href="https://www.openai.com/research/"><img src="https://img.shields.io/badge/Gen%20AI-OpenAI-red.svg" alt="Gen AI" style="margin: 5px;"></a>
<a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/license-MIT-brightgreen.svg" alt="License" style="margin: 5px;"></a>

</div>

<hr>

  ![Video GIF](static/Video.gif)

<hr>

<p> 
Travel Alchemy is a user-friendly web application designed to simplify travel planning by generating personalized itineraries. Users can easily input their starting location, dream destination, travel dates, and any specific preferences to create tailored travel plans. The app features an intuitive interface that presents itineraries in a structured, visually appealing format, enhanced by Markdown support. Users benefit from suggestions for accommodations and local attractions, making it easy to explore new destinations. Additionally, Travel Alchemy links to popular hotel and flight booking platforms, streamlining travel arrangements. Overall, Travel Alchemy empowers users to plan their adventures with confidence and ease.
</p>

## Table of Contents

- [Technologies Used](#technologies-used)
- [Key Features](#key-features)
  - [1. Functionality](#1-functionality)
  - [2. Code Quality](#2-code-quality)
  - [3. Creativity](#3-creativity)
  - [4. Approach](#4-approach)
  - [5. Solution](#5-solution)
  - [6. Additional Important Features](#6-additional-important-features)
- [Installation](#installation)
- [Usage](#usage)
- [Future Scalability](#future-scalability)
- [Contributing](#contributing)
- [License](#license)


## GitHub File Structure

```
/root
│
├── /static            # Folder for static files like CSS, JS, images
│
├── /templates         # Folder for HTML templates
│   ├── index.html     # Home page
│   └── welcome.html   # Welcome page
│
├── /instance          # Folder for instance-specific configurations
│   └── database.db    # SQLlite Database for storing User Data
│
├── app.py             # Main Flask application file
├── genai.py           # File for AI-related code (assuming using a generative AI feature)
├── .env               # Environment variables file (e.g., API keys, DB configs)
├── requirements.txt   # List of required dependencies (Flask, AI libraries, etc.)
└── README.md          # Project overview and setup instructions
```

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript (with Bootstrap for styling)
- **Markdown**: markdown-it for converting itinerary text to HTML
- **Environment Variables**: Manage sensitive information

## Key Features

### 1. Functionality

- The application effectively meets all specified requirements by allowing users to generate personalized travel itineraries.
- Users can provide essential information such as starting location, destination, travel dates, and additional preferences.
- Secure user authentication is implemented through a login and registration system, ensuring that users can access their saved itineraries and personal information securely.

### 2. Code Quality

- The codebase is clean, well-structured, and adheres to best practices in software development, making it easy to read and maintain.
- Comprehensive comments and documentation are provided throughout the code, enhancing understanding for future developers and contributors.

### 3. Creativity

- The application includes unique features that enhance user experience, such as support for **Markdown** formatting in the itinerary instructions, allowing users to customize their itineraries visually with lists, headers, and other formatting elements.
- The use of a visually appealing layout, with styled containers and responsive design elements, contributes to an enjoyable user experience.

### 4. Approach

- The application employs a logical and systematic approach to problem-solving. It gathers user input through a structured form and dynamically generates itineraries based on the submitted information.
- The integration of **external booking resources** enhances the application's utility, making it a one-stop solution for travel planning.

### 5. Solution

- The solution effectively addresses the challenge of creating a personalized travel itinerary generator, providing users with a seamless, interactive experience.
- By integrating additional features such as external booking links and a user-friendly interface, the application offers significant value to users, encouraging them to engage more deeply with their travel planning.

### 6. Additional Important Features

- **Welcome Page**: The application includes a dedicated welcome page for user login and registration, enhancing usability and access control.
- **Dynamic Itinerary Generation**: Users receive immediate feedback and a well-formatted itinerary upon submission, ensuring clarity and ease of use.
- **Responsive Design**: The application is designed to function optimally across various devices, ensuring accessibility and user satisfaction.
- **Logout Functionality**: Secure session management through a logout feature protects user data and privacy.

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/Djain318/Travel_Alchemy.git
   ```

2. **Navigate to the project directory:**

   ```bash
   cd travel-alchemy
   ```

3. **Set up a virtual environment:**

   - For macOS/Linux:
     ```bash
     python3 -m venv .venv
     ```
   - For Windows:
     ```bash
     py -3 -m venv .venv
     ```

4. **Activate the virtual environment:**

   - For macOS/Linux:
     ```bash
     . .venv/bin/activate
     ```
   - For Windows:
     ```bash
     .venv\Scripts\activate
     ```

5. **Install the required packages:**

   ```bash
   pip freeze > requirements.txt
   ```

6. **Create a `.env` file with your API keys:**
   ```bash
   "# API Key for Gemini
   GEMINI_API_KEY=your_api_key
   # Secret Key for your application
   SECRET_KEY=your_secret_key"
   ```

## Usage

1. **Run the application:**

   ```bash
   flask run
   ```

2. **Open your web browser and navigate to:**
   ```
   http://127.0.0.1:5000/
   ```

## Future Scalability

The application is structured to allow for easy addition of features, such as:

- Integrating **external APIs** for real-time data (flights, weather, etc.).
- Adding user accounts for saving itineraries.
- Allowing users to customize their itineraries based on preferences (cultural experiences, food, adventure).

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
