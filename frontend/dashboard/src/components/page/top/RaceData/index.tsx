import {
  Table,
  TableBody,
  TableCaption,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from '@/components/ui/table'

const races = [
  {
    id: '202406020409',
    raceName: '湾岸ステークス',
    racePlace: '中山',
    numberOfEntries: '14',
    date: '2024年3月3日',
  },
  {
    id: '202406020408',
    raceName: '4歳以上2勝クラス',
    racePlace: '中山',
    numberOfEntries: '11',
    date: '2024年3月3日',
  },
  {
    id: '202406020406',
    raceName: '3歳未勝利',
    racePlace: '中山',
    numberOfEntries: '18',
    date: '2024年3月3日',
  },
  {
    id: '202406020405',
    raceName: '3歳未勝利',
    racePlace: '中山',
    numberOfEntries: '16',
    date: '2024年3月3日',
  },
]

export const RaceResults = () => {
  return (
    <div className="overflow-auto px-8 py-4">
      <Table>
        <TableCaption>Only 4 past race data is displayed.</TableCaption>
        <TableHeader>
          <TableRow>
            <TableHead>Race name</TableHead>
            <TableHead>Race place</TableHead>
            <TableHead>Number of entries</TableHead>
            <TableHead className="text-right">Date</TableHead>
          </TableRow>
        </TableHeader>
        <TableBody>
          {races.map((race) => (
            <TableRow key={race.id}>
              <TableCell className="font-medium">{race.raceName}</TableCell>
              <TableCell className="text-center">{race.racePlace}</TableCell>
              <TableCell className="text-center">
                {race.numberOfEntries}
              </TableCell>
              <TableCell className="text-right">{race.date}</TableCell>
            </TableRow>
          ))}
        </TableBody>
      </Table>
    </div>
  )
}
