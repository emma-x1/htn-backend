# htn-backend

Hack the North backend challenge submission!

## Design Decisions and Assumptions

1. **Database Choice**: I chose to use SQLite because of its simplicity and the fact that it was pre-installed. 

2. **Badge Code System**: Assumes that each user has a unique badge code that serves as their primary identifier, emails are unique, name is not null. Some data had no badge code (likely by mistake), so I removed the data from the final dataset.

3. **Timestamp Handling**: Activity scans are automatically timestamped using SQLite's datetime('now') function, assuming the server's timezone is appropriate for the event.

4. **Partial Updates**: The update endpoint allows partial updates, meaning you can update individual fields without affecting others.

5. **Data Validation**: Basic validation is implemented, but in a production environment, I'd add more robust validation and error handling.

## Security Considerations

1. The current implementation doesn't include authentication/authorization - this should be added for production use.
2. Input validation should be enhanced for production deployment.
3. Consider adding rate limiting for endpoints.

## Future Improvements

1. Add user authentication and authorization
2. Implement input validation middleware
3. Add endpoint for bulk operations
4. Include more detailed error handling
5. Add logging system
6. Implement caching for frequently accessed data
