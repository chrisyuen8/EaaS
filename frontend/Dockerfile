# Use Node.js image
FROM node:18-alpine

WORKDIR /app

# Copy and install dependencies
COPY . .
RUN npm install
RUN npm run build

# Expose port
EXPOSE 3000

# Start the frontend
CMD ["npm", "start"]
