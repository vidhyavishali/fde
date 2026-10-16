DROP TABLE IF EXISTS care_interventions;
DROP TABLE IF EXISTS patient_encounters;

CREATE TABLE patient_encounters (
    encounter_id        BIGSERIAL PRIMARY KEY,
    patient_nbr         VARCHAR(50) NOT NULL,
    age                 INTEGER,
    time_in_hospital    INTEGER,
    number_inpatient    INTEGER,
    number_emergency    INTEGER,
    number_outpatient   INTEGER,
    num_medications     INTEGER,
    readmitted          BOOLEAN DEFAULT FALSE,
    risk_score          NUMERIC(5,2),
    risk_level          VARCHAR(20)
);

Drop Table IF Exists 

CREATE TABLE care_interventions (
    intervention_id     BIGSERIAL PRIMARY KEY,
    encounter_id        BIGINT NOT NULL,
    status              VARCHAR(50),
    assigned_to         VARCHAR(100),
    notes               TEXT,

    CONSTRAINT fk_care_interventions_encounter
        FOREIGN KEY (encounter_id)
        REFERENCES patient_encounters(encounter_id)
        ON DELETE CASCADE
);