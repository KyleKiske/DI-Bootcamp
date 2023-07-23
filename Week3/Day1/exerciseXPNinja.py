#Exercise 1 : Call History

class Phone: 
    def __init__(self, phone_number):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []

    def call(self, other_phone):
        call = f"{self.phone_number} called {other_phone.phone_number}"
        print(call)
        self.call_history.append(call)
        other_phone.call_history.append(call)
    def show_call_history(self):
        print(self.call_history)
    def send_message(self, other_phone, content):
        message = {
            "to" : other_phone.phone_number,
            "from" : self.phone_number,
            "content" : content
        }
        print(message)
        self.messages.append(message)
        other_phone.messages.append(message)
    
    def show_outgoing_messages(self):
        outgoing_messages = []
        for mess in self.messages:
            if mess["from"] == self.phone_number:
               outgoing_messages.append(mess)
        print(f"{self.phone_number} OUTGOING MESSAGES:")
        print(outgoing_messages)
    def show_incoming_messages(self):
        incoming_messages = []
        for mess in self.messages:
            if mess["to"] == self.phone_number:
               incoming_messages.append(mess)
        print(f"{self.phone_number} INCOMING MESSAGES:")
        print(incoming_messages)
    def show_messages_from(self, other_phone):
        messages_from = []
        for mess in self.messages:
            if mess["from"] == other_phone.phone_number:
               messages_from.append(mess)
        print(f"{self.phone_number} INCOMING MESSAGES FROM {other_phone.phone_number}:")
        print(messages_from)

puhel = Phone(1234)
gnusmas = Phone(5678)
two_minus = Phone(90)

puhel.call(gnusmas)
puhel.call(gnusmas)
puhel.call(two_minus)
gnusmas.call(puhel)

puhel.show_call_history()
gnusmas.show_call_history()
two_minus.show_call_history()

puhel.send_message(gnusmas, "AMOGUS")
puhel.send_message(two_minus, "SUS")
gnusmas.send_message(puhel, "YEAH")
two_minus.send_message(puhel, "HUH?")

puhel.show_incoming_messages()
puhel.show_outgoing_messages()
two_minus.show_outgoing_messages()
two_minus.show_incoming_messages()


puhel.show_messages_from(gnusmas)
puhel.show_messages_from(two_minus)