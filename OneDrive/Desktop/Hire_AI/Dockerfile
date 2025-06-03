# Build frontend
FROM node:18-alpine as frontend-builder
WORKDIR /app/frontend
COPY hire-ai/package*.json ./
RUN npm install
COPY hire-ai/ .
RUN npm run build

# Python backend
FROM python:3.9-slim
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy backend files
COPY backend/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy backend code
COPY backend/ .

# Copy built frontend
COPY --from=frontend-builder /app/frontend/dist /app/static

# Install serve to serve the frontend
RUN pip install serve

# Expose port
EXPOSE 8000

# Start both frontend and backend
CMD ["sh", "-c", "serve -s /app/static & uvicorn main:app --host 0.0.0.0 --port 8000"] 