import type { Encounter } from "../types/Encounter"

export function populateEncountersTable(encounters: Encounter[]): void
{
    const tableBody = document.getElementById("encounters-table-body")
    if (!tableBody) return
    tableBody.innerHTML = ""
    encounters.forEach(encounter => {
        const row = document.createElement("tr")
        row.innerHTML = `
            <td>${encounter.encounter_id}</td>
            <td>${encounter.patient_nbr}</td>
            <td>${encounter.age}</td>
            <td>${encounter.time_in_hospital}</td>
            <td>${encounter.number_inpatient}</td>
            <td>${encounter.number_outpatient}</td>
            <td>${encounter.number_emergency}</td>
            <td>${encounter.num_medications}</td>
            <td>${encounter.readmitted ?? ""}</td>
            <td>${encounter.risk_score}</td>
            <td>${encounter.risk_level}</td>
        `
        tableBody.appendChild(row)
    })
}