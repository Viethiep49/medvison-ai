-- MedVision AI Database Initialization

-- Create database (if running manually)
-- CREATE DATABASE medvision_db;

-- Connect to database
\c medvision_db;

-- Create predictions table
CREATE TABLE IF NOT EXISTS predictions (
    id VARCHAR(255) PRIMARY KEY,
    filename VARCHAR(500) NOT NULL,
    patient_id VARCHAR(255),

    -- Predictions stored as JSONB for flexibility
    predictions JSONB NOT NULL,
    bounding_boxes JSONB,

    -- Metadata
    model_version VARCHAR(50) NOT NULL,
    confidence_score FLOAT,
    processing_time FLOAT,

    -- Timestamps
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE,

    -- File paths
    image_path VARCHAR(500),
    result_image_path VARCHAR(500)
);

-- Create indexes
CREATE INDEX idx_predictions_patient_id ON predictions(patient_id);
CREATE INDEX idx_predictions_created_at ON predictions(created_at DESC);
CREATE INDEX idx_predictions_model_version ON predictions(model_version);

-- Create users table (for future authentication)
CREATE TABLE IF NOT EXISTS users (
    id SERIAL PRIMARY KEY,
    username VARCHAR(100) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    hashed_password VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    role VARCHAR(50) DEFAULT 'viewer',
    is_active BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_login TIMESTAMP WITH TIME ZONE
);

-- Create index on users
CREATE INDEX idx_users_username ON users(username);
CREATE INDEX idx_users_email ON users(email);

-- Create statistics view
CREATE OR REPLACE VIEW prediction_statistics AS
SELECT
    DATE(created_at) as date,
    COUNT(*) as total_predictions,
    AVG(confidence_score) as avg_confidence,
    AVG(processing_time) as avg_processing_time,
    model_version
FROM predictions
GROUP BY DATE(created_at), model_version
ORDER BY date DESC;

-- Grant permissions
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO medvision;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO medvision;
