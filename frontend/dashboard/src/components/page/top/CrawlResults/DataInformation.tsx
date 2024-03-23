import { Database } from 'lucide-react'
import { BlurCard } from '@/components/ui/BlurCard'

export const DataInformation = () => {
  return (
    <BlurCard className="flex h-full w-full flex-col items-center">
      <div className="flex items-center justify-center gap-4 p-2">
        <div className="rounded-lg border p-2">
          <Database className="h-4 w-4" />
        </div>
        <div className="text-lg font-bold">
          <p>取得済みデータ</p>
        </div>
      </div>
      <div className="flex w-full flex-col gap-2">
        <div className="flex justify-between">
          <div className="flex w-1/2 flex-col items-center">
            <div className="flex items-end gap-1">
              <p className="text-lg font-bold">4941</p>
              <p className="text-xs">件</p>
            </div>
            <p className="text-xs text-gray-500">全レースデータ件数</p>
          </div>
          <div className="flex w-1/2 flex-col items-center">
            <div className="flex items-end gap-1">
              <p className="text-lg font-bold">64222</p>
              <p className="text-xs">件</p>
            </div>
            <p className="text-xs text-gray-500">全出馬結果件数</p>
          </div>
        </div>
        <div className="flex flex-col items-center">
          <p className="font-bold">2024年03月05日 2回中山4日目</p>
          <p className="font-bold"> 3歳未勝利</p>
          <p className="text-xs text-gray-500">取得済み最新レースデータ</p>
        </div>
      </div>
    </BlurCard>
  )
}
