import { FC } from 'react'
import IconComponent from './IconComponent'

interface HorseEntryProps {
  index: number
  number: string
  name: string
  percentage: string
}

export const HorseEntry: FC<HorseEntryProps> = ({
  index,
  number,
  name,
  percentage,
}) => {
  return (
    <div className="flex items-center gap-2">
      <IconComponent index={index} />
      <p>{number}</p>
      <p>{name}</p>
      <p>{percentage}%</p>
    </div>
  )
}
