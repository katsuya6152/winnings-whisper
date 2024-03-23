import { History } from 'lucide-react'
import { BlurCard } from '@/components/ui/BlurCard'

export const CrawledTime = () => {
  return (
    <BlurCard className="flex h-full w-full flex-col items-center gap-2">
      <div className="flex items-center justify-center gap-2">
        <div className="rounded-lg border p-2">
          <History className="h-4 w-4" />
        </div>
        <div className="flex flex-col items-center">
          <p className="font-bold">取得時間</p>
          <div className="flex items-end">
            <p className="text-2xl font-bold">13</p>
            <p className="align-bottom">秒</p>
          </div>
        </div>
      </div>
      <div className="flex flex-col items-center">
        <p className="font-bold">2024/03/23/16:00:46</p>
        <p className="text-xs text-gray-500">取得開始時刻</p>
        <p className="font-bold">2024/03/23/16:00:59</p>
        <p className="text-xs text-gray-500">取得終了時刻</p>
      </div>
    </BlurCard>
  )
}
