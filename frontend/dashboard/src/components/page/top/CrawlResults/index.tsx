import { CrawledTime } from './CrawledTime'
import { RefineCriteria } from './RefineCriteria'
import { ExitReason } from './ExitReason'
import { DataInformation } from './DataInformation'

export const CrawlResults = () => {
  return (
    <div className="px-8 py-4">
      <div className="grid grid-cols-2 place-items-center gap-2">
        <CrawledTime />
        <RefineCriteria />
        <ExitReason />
        <DataInformation />
      </div>
    </div>
  )
}
