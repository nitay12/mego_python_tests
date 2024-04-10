class Time:
    def __init_(self, hour, minute):
        self.hour = hour
        self.minute = minute

    def before(other):
        pass

    def add_five_minutes():
        pass


class Message:
    def __init__(self, sender, subject, content, receiving_time, has_attachment):
        self.sender = sender
        self.subject = subject
        self.content = content
        self.receiving_time = receiving_time
        self.has_attachment = has_attachment

    def reply(self, text):
        return Message("support@uni.ac.il", -(self.subject), self.content + " " + text, self.receiving_time.add_five_minutes(), False)


class MailBox:
    def __init__(self):
        self.inbox = []
        self.no_of_mes = len(self.inbox)
    def how_many_between_times(self, first, second):
        counter = 0
        for message in self.inbox:
            if first.before(message.receiving_time) and message.receiving_time.before(second):
                counter += 1
        return counter

    def most_popular_subject(self):
        messages_dict = {1:0,2:0,3:0,4:0,5:0,6:0,7:0,8:0,9:0,10:0,11:0,12:0}
        for message in self.inbox:
            messages_dict[message.subject] += 1
        max = 0
        pop_sub = 1
        for subject, value in messages_dict.items():
            if value > max:
                max = value
                pop_sub = subject
        return pop_sub