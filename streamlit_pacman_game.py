
import streamlit as st
from random import choice

class Game:
    def __init__(self, level=1, score=0, word_pairs=None):
        if word_pairs is None:
            word_pairs = [("你好", "好"), ("我叫", "叫"), ("再見", "見"), ("什麼", "麼"), ("名字", "字"), ("你叫", "叫")]
        self.level = level
        self.score = score
        self.word_pairs = word_pairs
        self.current_pair = None
        self.next_word_pair()

    def next_word_pair(self):
        if self.word_pairs:
            self.current_pair = self.word_pairs.pop(0)

    def update_game(self, target_character):
        if self.current_pair and target_character == self.current_pair[1]:
            self.score += 10  # Increment score
            self.next_word_pair()  # Move to next word pair
            if len(self.word_pairs) == 0:
                self.level_up()
            return True
        return False

    def level_up(self):
        self.level += 1
        # Reset word pairs for the new level (can be modified to increase difficulty)
        self.word_pairs = [("你好", "好"), ("我叫", "叫"), ("再見", "見"), ("什麼", "麼"), ("名字", "字"), ("你叫", "叫")]
        self.next_word_pair()

# Streamlit app
def main():
    st.title("Mandarin Pac-Man Game")
    game = Game()

    if 'score' not in st.session_state:
        st.session_state['score'] = game.score
    if 'level' not in st.session_state:
        st.session_state['level'] = game.level
    if 'current_pair' not in st.session_state:
        st.session_state['current_pair'] = game.current_pair

    st.write(f"Level: {st.session_state['level']}")
    st.write(f"Score: {st.session_state['score']}")
    st.write(f"Current Word Pair: {st.session_state['current_pair'][0]}")

    # Placeholder for game interaction
    if st.button("Collect Character"):
        # Simulate collecting a character (this should be replaced with actual game logic)
        collected_character = choice(["好", "叫", "見", "麼", "字", "叫"])
        if game.update_game(collected_character):
            st.session_state['score'] = game.score
            st.session_state['current_pair'] = game.current_pair
            if game.word_pairs == []:
                st.session_state['level'] = game.level

    # Updating the display
    st.write(f"Updated Score: {st.session_state['score']}")
    st.write(f"Updated Level: {st.session_state['level']}")
    st.write(f"Updated Word Pair: {st.session_state['current_pair'][0] if st.session_state['current_pair'] else 'None'}")

if __name__ == "__main__":
    main()
