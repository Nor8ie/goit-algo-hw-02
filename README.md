TASK 1:
You are to develop a program that simulates the acceptance and processing of requests: the program should automatically generate new requests (identified by a unique number or other data), add them to the queue, and then sequentially remove them from the queue for "processing", thus simulating the work of a service center.
Here is the pseudo-code for a task using a queue (Queue from the queue module in Python) for a request processing system.

This pseudocode uses two main functions: generate_request(), which generates new requests and adds them to the queue, and process_request(), which processes requests by removing them from the queue. The main program loop performs these functions, simulating a constant flow of new requests and their processing.

TASK 2: 
Your task is to develop a function that takes a string as input, adds all its characters to a two-way queue (deque from the collections module in Python), and then compares the characters at both ends of the queue to determine if the string is a palindrome. The program should correctly handle both even and odd-numbered strings and be case and space-insensitive.
