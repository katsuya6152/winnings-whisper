import { Filter } from 'lucide-react'
import { BlurCard } from '@/components/ui/BlurCard'
import { Badge } from '@/components/ui/badge'

export const RefineCriteria = () => {
  return (
    <BlurCard className="flex h-full w-full flex-col items-center gap-2">
      <div className="flex items-center justify-center gap-4">
        <div className="rounded-lg border p-2">
          <Filter className="h-4 w-4" />
        </div>
        <div className="text-lg font-bold">
          <p>絞り込み条件</p>
        </div>
      </div>
      <div className="flex h-full flex-col items-start justify-center gap-2">
        <div className="flex gap-2">
          <p>競走種別:</p>
          <div className="flex gap-2">
            <Badge variant="turf">芝</Badge>
            <Badge variant="unselected">ダート</Badge>
            <Badge variant="unselected">障害</Badge>
          </div>
        </div>
        <div className="flex justify-center gap-2">
          <p>競馬場: </p>
          <div className="grid grid-cols-5 place-items-center gap-2">
            <Badge variant="unselected">札幌</Badge>
            <Badge variant="unselected">函館</Badge>
            <Badge variant="unselected">福島</Badge>
            <Badge variant="unselected">新潟</Badge>
            <Badge variant="selectedRacePlace">東京</Badge>
            <Badge variant="selectedRacePlace">中山</Badge>
            <Badge variant="selectedRacePlace">中京</Badge>
            <Badge variant="selectedRacePlace">京都</Badge>
            <Badge variant="selectedRacePlace">阪神</Badge>
            <Badge variant="unselected">小倉</Badge>
          </div>
        </div>
        <div className="flex gap-2">
          <p>距離:</p>
          <p className="font-bold">1600m ~ 3200m</p>
        </div>
      </div>
    </BlurCard>
  )
}
