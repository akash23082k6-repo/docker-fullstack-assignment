
# Use Node.js official lightweight image
FROM node:20-alpine

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy application source code
COPY . .

# Expose frontend port
EXPOSE 3000

# Start the frontend application
CMD ["npm", "start"]
