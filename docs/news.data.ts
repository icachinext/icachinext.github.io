import { createContentLoader } from 'vitepress'

interface NewsItem {
    title: string
    url: string
    date: string
    excerpt: string | undefined
    cover: string | undefined
}

declare const data: NewsItem[]
export { data }

export default createContentLoader('news/*.md', {
    includeSrc: false, // We don't need raw source
    render: true,     // We want excerpts rendered? No, excerpt: true usually gets raw string.
    excerpt: true,
    transform(raw): NewsItem[] {
        return raw
            .map(({ url, frontmatter, excerpt }) => ({
                title: frontmatter.title,
                url,
                excerpt,
                date: frontmatter.date,
                cover: frontmatter.cover
            }))
            .sort((a, b) => {
                return +new Date(b.date) - +new Date(a.date)
            })
    }
})
