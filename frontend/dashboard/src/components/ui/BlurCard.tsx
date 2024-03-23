import * as React from 'react'
import { Card } from '@/components/ui/card'
import { cn } from '@/lib/utils'

const BlurCard = React.forwardRef<
  HTMLDivElement,
  React.HTMLAttributes<HTMLDivElement>
>(({ className, ...props }, ref) => (
  <Card
    ref={ref}
    className={cn(
      'rounded-md border-none bg-black/30 p-2 text-white shadow-lg backdrop-blur-lg',
      className,
    )}
    {...props}
  />
))
BlurCard.displayName = 'BlurCard'

export { BlurCard }
