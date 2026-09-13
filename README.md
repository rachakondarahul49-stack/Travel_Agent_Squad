# Travel_Agent_Squad

## Squad
- TL: Rachakonda Rahul (Architecture & Integration)
- Marigadda Sathwika — Flight Search & Booking
- Donthi Sumegha Reddy — Hotel Search & Booking
- Dubbaka Sanjana — Itinerary Planner (RAG)
- Gundla Sriharsha — Budget & Expense Estimator
- Singarapu Jayasree — User Preference Agent
- Bhavya Neeradi — Weather & Local Info
- Butti Srimannarayana — Orchestrator / Chat Interface

## Work Breakdown Structure (v1)

| # | Module | Owner | Domain | Data Needed | Tools | Output |
|---|--------|-------|--------|--------------|-------|--------|
| 1 | Flight Search & Booking | Sathwika | Find/compare flights for dates & route | Flight schedules, prices | Skyscanner/Amadeus API (or mock) | Ranked flight options |
| 2 | Hotel Search & Booking | Sumegha Reddy | Find hotels matching budget/preferences | Hotel listings, ratings | Booking.com/Places API (or mock) | Ranked hotel options |
| 3 | Itinerary Planner (RAG) | Sanjana | Day-wise plans from destination knowledge | Destination guides, attractions | ChromaDB + RAG | Day-wise itinerary |
| 4 | Budget & Expense Estimator | Sriharsha | Estimate trip cost, flag overruns | Flight/hotel/activity prices | Calculator tool, LLM | Cost breakdown |
| 5 | User Preference Agent | Jayasree | Capture & apply preferences | User inputs | LLM + memory | Personalized filters |
| 6 | Weather & Local Info | Bhavya | Weather, visa, safety info | Weather API, visa data | Web search/weather API | Contextual alerts |
| 7 | Orchestrator / Chat Interface | Srimannarayana | Route queries, combine results | Outputs from 1-6 | LangChain/CrewAI | Unified chat response |
