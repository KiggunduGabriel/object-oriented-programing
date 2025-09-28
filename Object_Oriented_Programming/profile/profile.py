# profile.py

class Profile:
    def __init__(self, name, favorite_language, hobby, tech_stack, github_username, fun_fact):
        self.name = name
        self.favorite_language = favorite_language
        self.hobby = hobby
        self.tech_stack = tech_stack
        self.github_username = github_username
        self.fun_fact = fun_fact

    def introduce(self):
        return f"Hi, I'm {self.name}. I love {self.favorite_language} and my hobby is {self.hobby}. Fun fact: {self.fun_fact}"

    def show_stack(self):
        stack = ", ".join(self.tech_stack)
        return f"My tech stack includes: {stack}"

    def github_link(self):
        return f"https://github.com/{self.github_username}"


# Example usage
if __name__ == "__main__":
    # create your profile here
    my_profile = Profile(
        name="Gabriel",
        favorite_language="Python",
        hobby="reading tech blogs",
        tech_stack=["Python", "Django", "Git", "JavaScript"],
        github_username="KiggunduGabriel",
        fun_fact="I can debug faster with coffee ☕"
    )

    print(my_profile.introduce())
    print(my_profile.show_stack())
    print(my_profile.github_link())
