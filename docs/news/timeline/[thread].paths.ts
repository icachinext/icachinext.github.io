import conferenceData from '../../../data/conferences.json'

export default {
  paths: () => conferenceData.map(conference => ({
    params: { thread: conference.thread },
    content: `# ${conference.shortTitle} Timeline\n\n<NewsTimeline />`
  }))
}
