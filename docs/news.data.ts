import { createContentLoader } from 'vitepress'

interface NewsItem {
    title: string
    url: string
    date: string
    excerpt: string | undefined
    cover: string | undefined
    tags: string[]
}

declare const data: NewsItem[]
export { data }

export default createContentLoader(['news/*.md', 'en/news/*.md'], {
    includeSrc: false,
    render: false,
    excerpt: true,
    transform(raw): NewsItem[] {
        return raw
            .filter(({ frontmatter }) => frontmatter.title)
            .map(({ url, frontmatter, excerpt }) => ({
                title: frontmatter.title,
                url,
                excerpt: frontmatter.excerpt || excerpt,
                date: frontmatter.date,
                cover: frontmatter.cover,
                tags: Array.isArray(frontmatter.tags) ? frontmatter.tags : []
            }))
            .sort((a, b) => +new Date(b.date) - +new Date(a.date))
    }
})
