import conferenceData from '../data/conferences.json'

export interface ConferenceThread {
  year: number
  shortTitle: string
  thread: string
  timelinePinned?: boolean
  title: string
  subtitle?: string
  location: string
  dates?: string
  link: string
  image: string
}

export const conferenceThreads = conferenceData as ConferenceThread[]

export function findConferenceThread(thread?: string) {
  if (!thread) return undefined
  return conferenceThreads.find(conference => conference.thread === thread)
}

export function timelinePath(thread: string, isEn: boolean) {
  return `${isEn ? '/en' : ''}/news/timeline/${thread}`
}
