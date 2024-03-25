import { CrawledTime } from './CrawledTime'
import { RefineCriteria } from './RefineCriteria'
import { ExitReason } from './ExitReason'
import { DataInformation } from './DataInformation'

export const CrawlResults = () => {
  return (
    <div className="px-4 py-4 sm:px-8">
      <p className="mb-2 text-center text-xl font-bold sm:hidden">
        クロール結果
      </p>
      <div className="grid h-full w-full grid-cols-1 place-items-center gap-2 sm:grid-cols-2">
        <CrawledTime />
        <RefineCriteria />
        <ExitReason />
        <DataInformation />
      </div>
    </div>
  )
}
