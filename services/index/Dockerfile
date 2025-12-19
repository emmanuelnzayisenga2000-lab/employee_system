FROM node:18-alpine

WORKDIR /app

# Copy package files first to install deps
COPY package.json package-lock.json* ./
RUN npm install --production

# Copy source
COPY . .

ENV PORT=8080
EXPOSE 8080

CMD ["node", "index.js"]
