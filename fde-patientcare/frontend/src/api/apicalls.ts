const URL_ENDPOINT = 'http://127.0.0.1:8000'
const ENCOUNTER_PATH = '/encounters'
const INTERVENTION_PATH = '/interventions'


export async function getEncounters()
{
    const requestUrl = URL_ENDPOINT + ENCOUNTER_PATH
    const response = await fetch(requestUrl) //returns a promise
    console.log(response)
    const data = await response.json()
    console.log(data)
    return data

} // use await whereever you use promise or json from response.
//  response.status or response.ok can be used without await . read what is promis and why


export async function getCareQueue()
{
    const response = await fetch('http://127.0.0.1:8000/care-queue?limit=10')
    console.log(response)
    const data = await response.json()
    console.log(data)
    return data
}

export async function addEncounter(patient_number: string, age: string, in_hospital_days: number, inpatient_visits: number, outpatient_visits: number, emergency_visits: number, medications: number)
{
 //   document.getElementById("encounter-form")


    const requestUrl = URL_ENDPOINT + ENCOUNTER_PATH
    const response = await fetch(requestUrl, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            patient_number,
            age,
            in_hospital_days,
            inpatient_visits,
            outpatient_visits,
            emergency_visits,
            medications
        })
    })
    console.log(response)
    
    const data = await response.json()
    console.log(data)
    return data
}

//addEncounter("12345", "19-35", 5, 2, 3, 1, 4)