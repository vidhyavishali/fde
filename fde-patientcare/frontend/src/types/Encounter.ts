export interface Encounter {
    encounter_id: number
    patient_nbr: string
    age: string
    time_in_hospital: number
    number_inpatient: number
    number_emergency: number
    number_outpatient: number
    num_medications: number
    readmitted: string
    risk_score: number
    risk_level: string
}