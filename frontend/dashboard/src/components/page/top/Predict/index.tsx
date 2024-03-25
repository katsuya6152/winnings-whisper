import { Bot } from 'lucide-react'
import raceEntries from './raceEntries.json'
import { HorseEntry } from './HorseEntry'
import {
  Accordion,
  AccordionContent,
  AccordionItem,
  AccordionTrigger,
} from '@/components/ui/accordion'
import { Separator } from '@/components/ui/separator'

export const Predict = () => {
  return (
    <div className="p-4">
      <Separator className="mb-4 bg-gray-700 sm:hidden" />
      <div className="relative flex items-center justify-center gap-4">
        <div className="rounded-lg border p-2">
          <Bot className="h-4 w-4" />
        </div>
        <div className="font-bold">
          <p>予測</p>
        </div>
        <p className="bottom-0 right-0 hidden text-[10px] sm:absolute">
          ※予測はレース前日もしくは当日に更新されます
        </p>
      </div>
      <p className="my-2 text-center text-[10px] sm:hidden">
        ※予測はレース前日もしくは当日に更新されます
      </p>
      <div>
        <Accordion type="single" collapsible className="w-full">
          {raceEntries.map((entry, index) => (
            <AccordionItem key={index} value={`item-${index}`}>
              <AccordionTrigger>{entry.date}</AccordionTrigger>
              <AccordionContent className="flex flex-col gap-2">
                {entry.horses.map((horse, horseIndex) => (
                  <HorseEntry key={horseIndex} index={horseIndex} {...horse} />
                ))}
              </AccordionContent>
            </AccordionItem>
          ))}
        </Accordion>
      </div>
    </div>
  )
}
