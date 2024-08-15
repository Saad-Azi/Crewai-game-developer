# CrewAI Game Development and General Query Handler

This project leverages CrewAI and LangChain to handle both game development tasks and general queries. The system uses various specialized agents to process game development requests and a general-purpose agent for other inquiries.

## Features

- **Game Development Tasks**: Create, review, and evaluate game code using dedicated agents.
- **General Query Handling**: Respond to non-game development queries using a general-purpose agent.
- **Integration with OpenAI GPT-4**: Uses `ChatOpenAI` from LangChain for natural language understanding and processing.
- **Environment Configuration**: Loads environment variables using `dotenv`.

## Prerequisites

- Python 3.11.7
- `crewai` package
- `langchain_openai` package
- `python-dotenv` package

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Saad-Azi/crewai-game-developer.git
    cd your-repo
    ```

2. **Install the required packages**:
    ```bash
    poetry shell
    poetry install
    ```

3. **Set up environment variables**:
    - Create a `.env` file in the root of the project directory.
    - Add your OpenAI API key to the `.env` file:
      ```
      OPENAI_API_KEY=your_openai_api_key
      ```

## Usage

1. **Run the main script**:
    ```bash
    poetry run python main.py
    ```

2. **Provide Instructions**:
    - When prompted, enter a description for a game or a general query. The system will automatically classify the input and route it to the appropriate agents.

3. **Viewing Results**:
    - For game development tasks, the final code will be printed.
    - For general queries, the response to the query will be displayed.

## Code Overview

- `agents.py`: Defines different agents for handling game development tasks and general queries.
- `tasks.py`: Contains tasks for generating, reviewing, and evaluating game code, as well as handling general queries.
- `main.py`: Main script that initializes agents and tasks, handles user input, and processes the instructions accordingly.

## Example

### Game Development


- The script will process the game development request using the specialized game development agents and print the final game code.
- Use 'game' or 'develop' keyword in your prompt to execute the agents responsible for development.

### General Query


- The script will process the query using the general-purpose agent and print the response.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## Contact

For any questions or feedback, please contact sunnyaziz120@gmail.com

