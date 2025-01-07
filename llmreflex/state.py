
# state.py
import reflex as rx

class State(rx.State):
    """The app state."""

    # The current question being asked.
    question: str = ""

    # Keep track of the chat history as a list of (question, answer) tuples.
    chat_history: list[tuple[str, str]] = []

    def answer(self):
        """Handle the user's question."""
        # Basic response without OpenAI
        answer = "This is a basic response without using OpenAI."

        # Append the question and answer to the chat history.
        self.chat_history.append((self.question, answer))
        print(self.chat_history)

        # Clear the question input.
        self.question = ""
