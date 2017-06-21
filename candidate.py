class Candidate:

    def __init__(self, name):
        self.name = name
        self.education = []
        self.experience = []
        self.projects = {}
        self.other_experience = []
        self.skills = []

    def add_education(self, *args):
        for arg in args:
            self.education.append(arg)

    def add_experience(self, position):
        self.experience.append(position)

    def add_projects(self, projects_dict):
        self.projects.update(projects_dict)

    def add_other_experience(self, *args):
        for arg in args:
            self.other_experience.append(arg)

    def add_skills(self, skills_list):
        self.skills.extend(skills_list)


class Experience:

    def __init__(self, position, location, duration):
        self.position = position
        self.location = location
        self.duration = duration
        self.responsibilities = []

    def add_responsibilities(self, responsibilities_list):
        self.responsibilities.extend(responsibilities_list)
