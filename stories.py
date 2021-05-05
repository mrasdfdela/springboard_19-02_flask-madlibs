"""Madlibs Stories."""


class Story:
    """Madlibs story.

    To  make a story, pass a list of prompts, and the text
    of the template.

        >>> s = Story(["noun", "verb"],
        ...     "I love to {verb} a good {noun}.")

    To generate text from a story, pass in a dictionary-like thing
    of {prompt: answer, promp:answer):

        >>> ans = {"verb": "eat", "noun": "mango"}
        >>> s.generate(ans)
        'I love to eat a good mango.'
    """

    def __init__(self, title, words, text):
        """Create story with words and template text."""
        self.title = title
        self.prompts = words
        self.template = text

    def generate(self, answers):
        """Substitute answers into text."""

        text = self.template

        for (key, val) in answers.items():
            text = text.replace("{" + key + "}", val)

        return text


# Here's a story to get you started


fairy_tail = Story(
    "fairy_tail",
    ["place", "noun", "verb", "adjective", "plural_noun"],
    """Once upon a time in a long-ago {place}, there lived a
       large {adjective} {noun}. It loved to {verb} {plural_noun}."""
)

dad_libs = Story(
  "dad_libs",
  ["local_place","word_starting_with_H","verb","other_verb","occupation","type_of_business"],
  """Grandpa was born here in St. Louis at {local_place} in 1949. His middle initial is H., which stands for {word_starting_with_H}. In elementary school, he loved to play baseball, {verb}, and {other_verb} with his friends.In college he studied to become a(n) {occupation} because he wanted to work in the local {type_of_business} along with your Great-grandma Ellen."""
)

story_bank = [fairy_tail,dad_libs]
