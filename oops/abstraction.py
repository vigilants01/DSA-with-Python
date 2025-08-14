from abc import ABC,abstractmethod

class onlineExam(ABC):
    @abstractmethod
    def start(self):
        pass

class mathExam(onlineExam):
    def start(self):
        print("math exam")

class scienceExam(onlineExam):
    def start(self):
        print("science exam")

exams=[mathExam(),scienceExam()]

for exam in exams:
    exam.start()