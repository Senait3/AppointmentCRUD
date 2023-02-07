# AppointmentCRUD(Prototype)

Purpose of this program is to practice using a CRUD database in python to help users schedule an appointment with their care providers. The users can designate times, pick a provider, choose which center, and either cancel or append their appointment. The purpose of this is to eliminate the need for a third party to make appointments for users when they can create them on their own and not have to wait in a call line for them to reach a representative.

# SQLite

Using sqlite the information of doctors, operation hours, specialties, and locations are created and the users selections are stored. Once the selection is stored another user cannot make the same appointment with the same doctor. If the user would like to reschedule their appointment they have to go back and select the made appointment and swap it for an available time. If the user wants to cancel they will be asked if they want to reschedule instead if they decide to cancel the appointment then it will be done.
