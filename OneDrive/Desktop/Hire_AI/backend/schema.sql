 -- Create candidates table
CREATE TABLE IF NOT EXISTS candidates (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    skills TEXT[] DEFAULT '{}',
    experience JSONB[] DEFAULT '{}',
    education JSONB[] DEFAULT '{}',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc'::text, NOW()),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc'::text, NOW())
);

-- Create jobs table
CREATE TABLE IF NOT EXISTS jobs (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    title TEXT NOT NULL,
    company TEXT NOT NULL,
    description TEXT,
    skills TEXT[] DEFAULT '{}',
    location TEXT,
    type TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc'::text, NOW()),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc'::text, NOW())
);

-- Create applications table
CREATE TABLE IF NOT EXISTS applications (
    id UUID DEFAULT gen_random_uuid() PRIMARY KEY,
    candidate_id UUID REFERENCES candidates(id),
    job_id UUID REFERENCES jobs(id),
    status TEXT DEFAULT 'pending',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc'::text, NOW()),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT TIMEZONE('utc'::text, NOW()),
    UNIQUE(candidate_id, job_id)
);

-- Create function to update updated_at timestamp
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = TIMEZONE('utc'::text, NOW());
    RETURN NEW;
END;
$$ language 'plpgsql';

-- Create triggers for updated_at
CREATE TRIGGER update_candidates_updated_at
    BEFORE UPDATE ON candidates
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_jobs_updated_at
    BEFORE UPDATE ON jobs
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_applications_updated_at
    BEFORE UPDATE ON applications
    FOR EACH ROW
    EXECUTE FUNCTION update_updated_at_column();