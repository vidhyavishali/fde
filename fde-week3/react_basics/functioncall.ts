



const encounter1:PatientEncounter = {
    encounter_id: 1,
    patient_nbr: 1,
    age:40,
    risk_level: "LOW",
    status: "ACTIVE"
}
const encounter2:PatientEncounter = {
    encounter_id : 2,
   patient_nbr: 2,
    age : 50,
    risk_level : "HIGH",
    status: "ACTIVE"
}

const encounters:PatientEncounter[] = [encounter1,encounter2]

let  hardcoded_encounters =(encounter_id: number):PatientEncounter | undefined =>  {
    return encounters.find(encounter => encounter.encounter_id === encounter_id)

}

let get_all_encounters = ():PatientEncounter[] => {
    return encounters
}

console.log(hardcoded_encounters(1))