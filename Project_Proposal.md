Initial Database Project Proposal
Project Title
Community Tool Lending Library Management System

Application Overview
The proposed application is a community tool lending library where registered members can borrow shared equipment such as drills, ladders, gardening tools, and sewing machines. The database will help library staff track tools, members, reservations, loans, returns, and maintenance. The goal is to make borrowing reliable, reduce duplicate purchases, and keep equipment available and safe for the community.

Planned Entities
- Members: Member ID, name, contact information, join date, and membership status.
- Tools: Tool ID, name, category, condition, location, and availability status.
- Tool Categories: Category ID, category name, and description.
- Reservations: Reservation ID, member, tool, requested pickup date, and status.
- Loans: Loan ID, member, tool, checkout date, due date, return date, and loan status.
- Maintenance Records: Maintenance ID, tool, reported issue, service date, and repair status.
- Staff: Staff ID, name, role, and contact information.
These entities will be related so that a member can have multiple reservations and loans, while each tool can have a history of loans and maintenance activities.
SS
Business Processes Supported
1. Registering a member: Staff create a member record and activate the membership.
2. Adding a tool: Staff record a new tool, assign its category, and mark its initial condition and location.
3. Searching and reserving tools: Members check availability and request a tool for a future date.
4. Checking out a tool: Staff confirm eligibility, record the loan, and establish a due date.
5. Returning a tool: Staff record the return date, inspect the tool, and update availability.
6. Managing overdue loans: Staff identify overdue tools and contact members about returns.
7. Tracking repairs: Staff mark damaged tools unavailable, document maintenance, and return them to circulation when repaired.
Expected Value and Scope

The database will provide an accurate view of inventory, borrowing activity, and equipment condition. It will help prevent double bookings, support overdue-loan follow-up, and inform decisions about which tools to purchase or replace. The initial project focuses on one community lending location. Online payments, delivery services, and multiple branches are outside the initial scope but could be added later.

Initial Design Considerations

Each member and tool will have a unique identifier. A tool should not be checked out to two members at the same time. Tools undergoing maintenance should not be available for new loans. The detailed relationships, constraints, and table structure will be refined during the database design phase.
