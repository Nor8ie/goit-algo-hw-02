from queue import Queue
from random import randint

# Create a queue of applications
queue = Queue()


def generate_ticket_no():
    while True:
        ticket = randint(1, 1000)  # Chosen for this task a range up to 1000

        #Checking for ticket number to avoid duplicate numbering
        if ticket not in list(queue.queue): 
            return ticket


def generate_request():
    ticket = generate_ticket_no()
    queue.put(ticket)
    print(f"Ticket {ticket} has been added to the queue.\n")
    tickets_before = list(queue.queue)
    print(
        f"There are {len(tickets_before)} tickets waiting in the queue.\nThe list of tickets to process {tickets_before}.\n"
    )


def process_request():
    if not queue.empty():
        ticket = queue.get()
        tickets_after = list(queue.queue)
        print(">>>> PROCESSING <<<<\n")
        print(f"Ticket {ticket} was resolved.")
        print(
            f"There are {len(tickets_after)} tickets left in the queue.\nThe list of tickets awaiting processing {tickets_after}.\n"
        )
    else:
        print("There are no tickets left in the queue.\n")


# The main cycle of the program:
def main():
    print(
        """Welcome to the ticketing system for Customer Service requests:\n
          To continue, please choose one of the following options:
          >>> 1 to Accept/Generate the request)
          >>> 2 to Process a ticket from the queue.
          >>> 3 to Exit de system.\n"""
    )
    while True:
        command = input(
            "Please enter you option: 1 to generate a new ticket; 2 to process a ticket or 3 to exit: "
        )
        if command not in ["1", "2", "3"]:
            print("Please enter a valid option: 1, 2 or 3.")

        #Creating new ticket number one at a time
        elif command == "1":
            generate_request()

        #Processing tickets one at a time
        elif command == "2": 
            process_request()

        elif command == "3":
            print("\nThank you for using the ticketing system.")
            break


if __name__ == "__main__":
    main()
