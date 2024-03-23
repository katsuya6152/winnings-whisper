import React from 'react'
import { Disc2, Circle, Triangle } from 'lucide-react'

interface IconProps {
  index: number
}

const IconComponent: React.FC<IconProps> = ({ index }) => {
  switch (index) {
    case 0:
      return <Disc2 />
    case 1:
      return <Circle />
    default:
      return <Triangle />
  }
}

export default IconComponent
