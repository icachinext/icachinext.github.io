import { computed } from 'vue'
import { useData } from 'vitepress'
import siteZh from '../data/site.json'
import siteEn from '../data/site.en.json'
import resources from '../data/resources.json'

export function useSiteData() {
  const { lang } = useData()
  const isEn = computed(() => lang.value?.startsWith('en'))
  const site = computed(() => (isEn.value ? siteEn : siteZh))
  const resourceList = computed(() => (isEn.value ? resources.en : resources.zh))
  return { isEn, site, resourceList }
}
