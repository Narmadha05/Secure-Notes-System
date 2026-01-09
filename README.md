# Secure-Notes-System
Secure Notes System is a backend-focused project that demonstrates security-aware system design and analysis for handling sensitive user data. The project emphasizes how data is authenticated, protected, stored, and accessed.

# Key Components
- Backend API: Processes authentication and note operations
- Database: Stores user data and encrypted notes
- Authentication Layer: Session-based access control
- Encryption Layer: Encrypts note content before storage
- Logging: Records sensitive operations for traceability

# Data Flow Summary
1.  User submits credentials or note data to the backend
2.  Authentication is enforced before accessing protected routes
3.  Note content is encrypted prior to database storage
4.  Encrypted data is associated with the owning user
5.  Notes are decrypted and returned only to authorized user 
