import { CrawlResults } from '@/components/page/top/CrawlResults'
import { TrainingResults } from '@/components/page/top/TrainingResults'
import { RaceResults } from '@/components/page/top/RaceData'
import { Predict } from '@/components/page/top/Predict'

const TopPage = () => {
  return (
    <div
      className="grid grid-cols-1 bg-gradient-to-br from-[#0f0f0f]/50 via-gray-950
    to-gray-800 text-white sm:h-screen sm:grid-cols-2"
    >
      <CrawlResults />
      <TrainingResults />
      <RaceResults />
      <Predict />
    </div>
  )
}

export default TopPage
