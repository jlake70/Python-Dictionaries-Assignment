service_tickets = {}
ticket_counter = 1

def new_ticket(customer_name, issue):
    global ticket_counter
    ticket_id = ticket_counter
    service_tickets[ticket_id] = {"Customer Name": customer_name, "Issue": issue, "Status": "open"}
    ticket_counter += 1

    return ticket_id
   

def update_ticket(ticket_id):
    if ticket_id in service_tickets and service_tickets[ticket_id]["Status"] == "open":
        service_tickets[ticket_id]["Status"] = "closed"
        return True
       
    else:
        
        print("Invalid ticket number")
        

def display_tickets(service_tickets):
    for  ticket_id, service_tickets in service_tickets.items():
        print(f"Ticket Id:",  {ticket_id}, "Customer:", {service_tickets["Customer Name"]}, "Issue:", {service_tickets["Issue"]}, "Status:", {service_tickets["Status"]})




new_ticket("John", "log-in error")
new_ticket("Greg", "user not found")
update_ticket(ticket_id=2)
display_tickets(service_tickets)
print(service_tickets)