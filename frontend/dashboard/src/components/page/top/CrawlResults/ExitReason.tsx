import { HardDriveDownload } from 'lucide-react'
import { BlurCard } from '@/components/ui/BlurCard'
import { Badge } from '@/components/ui/badge'

export const ExitReason = () => {
  return (
    <BlurCard className="flex h-full w-full flex-col items-center">
      <div className="flex items-center justify-center gap-4 p-2">
        <div className="rounded-lg border p-2">
          <HardDriveDownload className="h-4 w-4" />
        </div>
        <div className="text-lg font-bold">
          <p>クロール結果</p>
        </div>
      </div>
      <div className="flex h-full items-center gap-10 p-2">
        <div className="flex flex-col items-center gap-1">
          <p className="font-bold text-green-500">exists in database</p>
          <p className="text-xs text-gray-500">クローラー停止理由</p>
        </div>
        <Badge variant="normalEnd">正常に終了</Badge>
      </div>
    </BlurCard>
  )
}
