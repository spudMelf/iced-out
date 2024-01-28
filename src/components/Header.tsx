// import {
//   Dialog,
//   DialogContent,
//   DialogDescription,
//   DialogHeader,
//   DialogTitle,
//   DialogTrigger,
// } from "@/components/ui/dialog";
import { Input } from "@/components/ui/input";
import { Button } from "./ui/button";

export default function Header() {
  return (
    <div className="flex justify-between align-middle p-2">
      <Input
        disabled
        type="email"
        placeholder="Title"
        className="w-[200px] bg-[#09090B] border-0 text-3xl text-[#E2E2E2]"
      />
      <div className="flex gap-2">
        <Input placeholder="Email" className="bg-[#212124] border-[#27272A]" />
        <Button className="bg-[#212124] p-2">Button 1</Button>
        <Button className="bg-[#212124] p-2">Button 1</Button>
        <Button className="bg-[#212124] p-2">Button 1</Button>
      </div>
    </div>
  );
}
