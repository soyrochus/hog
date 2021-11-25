
type Json = string | number | boolean | null | Json[] | { [key: string]: Json };
type KEvent = {name: string, data: Json}
type KEvents = Event[]

type TestResult = {success: boolean, error?: string}
type KEventsTest = (events: KEvents, expected: Json) => TestResult

