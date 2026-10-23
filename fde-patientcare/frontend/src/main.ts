import { getEncounters } from "./api/apicalls"
import { populateEncountersTable } from "./ui/ui"

async function init(): Promise<void> {
    const encounters = await getEncounters()
    populateEncountersTable(encounters)
}

init()